# load the required libraries
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os

# take environment variables from .env
load_dotenv()

# initialize the flask app
app = Flask(__name__)

# MongoDB values to establish connection
mongo_host = os.getenv('MONGODB_HOST')
mongo_port = os.getenv('MONGODB_PORT')
mongo_username = os.getenv('MONGODB_USERNAME')
mongo_password = os.getenv('MONGODB_PASSWORD')
mongo_database = os.getenv('MONGODB_DATABASE')
mongo_collection = os.getenv('MONGODB_COLLECTION')

# Informations about the software
version_number = os.getenv('VERSION_NUMBER')
author = os.getenv('AUTHOR')
release_date = os.getenv('RELEASE_DATE')
contact_mail=os.getenv('CONTACT_MAIL')

# MongoDB connection informations
client = MongoClient(host=mongo_host, port=int(mongo_port),
                     username=mongo_username, password=mongo_password)
db = client[mongo_database]
collection = db[mongo_collection]


@app.route('/')
def index():
    """Define the informations for the 'index.html' page

    Returns:
        index.html: send needed informations to the template, to render it with the rights informations
    """

    # Fetch all documents from the collection
    users = list(collection.find())

    # Define the number of items per page
    items_per_page = 8

    # Calculate the total number of pages
    total_pages = len(users) // items_per_page + \
        (1 if len(users) % items_per_page != 0 else 0)

    # Get the page number from the query parameters
    # default is set to 1 for the first display time, nor retrives the information from the browser
    page = request.args.get('page', default=1, type=int)

    # Calculate the starting and ending indexes for the current page
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    # Slice the users list to get the data for the current page
    paginated_users = users[start_index:end_index]

    # We send also the informations about the author, ...
    return render_template('index.html', paginated_users=paginated_users, total_pages=total_pages, current_page=page, version_number=version_number, author=author, release_date=release_date,contact_mail=contact_mail)


@app.route('/update/<string:user_id>', methods=['POST'])
def update(user_id):
    """Define what is performed when the 'update' button is pushed
    """
    # Retrieve form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    # age is converted as int to be stored, even it's an int on the webpage
    age = int(request.form['age'])

    # Update user in the collection
    collection.update_one({'_id': ObjectId(user_id)}, {'$set': {
                          'first_name_db': first_name, 'last_name_db': last_name, 'age_db': age}})

    # Send to the browser to stay on the current page - nor it doesn't stay on the right page
    return redirect(request.referrer)


# define what is performed when the 'update' button is pushed
@app.route('/delete/<string:user_id>')
def delete(user_id):

    # Delete user from the collection - simply with user_id
    collection.delete_one({'_id': ObjectId(user_id)})

    # Send to the browser to stay on current page - nor it doesn't stay on the right page
    return redirect(request.referrer)


# define what is performed when the 'add user' button is pushed
@app.route('/add', methods=['POST'])
def add():
    # Retrieve form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = int(request.form['age'])

    # Insert new user into the collection
    collection.insert_one({'first_name_db': first_name,
                          'last_name_db': last_name, 'age_db': age})

    # Calculate the total number of pages
    total_pages = (collection.count_documents({}) - 1) // 8 + 1

    return redirect(f'/?page={total_pages}')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded = True)
