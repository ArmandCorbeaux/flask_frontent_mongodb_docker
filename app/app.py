from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os

load_dotenv()

app = Flask(__name__)

# MongoDB connection
mongo_host = os.getenv('MONGODB_HOST')
mongo_port = os.getenv('MONGODB_PORT')
mongo_username = os.getenv('MONGODB_USERNAME')
mongo_password = os.getenv('MONGODB_PASSWORD')
mongo_database = os.getenv('MONGODB_DATABASE')
mongo_collection = os.getenv('MONGODB_COLLECTION')

client = MongoClient(host=mongo_host, port=int(mongo_port),
                     username=mongo_username, password=mongo_password)
db = client[mongo_database]
collection = db[mongo_collection]


@app.route('/')
def index():
    # Get the page number from the query parameters
    page = request.args.get('page', default=1, type=int)

    # Define the number of items per page
    items_per_page = 8

    # Calculate the starting and ending indexes for the current page
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    # Fetch all documents from the collection
    users = list(collection.find())

    # Slice the users list to get the data for the current page
    paginated_users = users[start_index:end_index]

    # Calculate the total number of pages
    total_pages = len(users) // items_per_page + \
        (1 if len(users) % items_per_page != 0 else 0)

    return render_template('index.html', paginated_users=paginated_users, total_pages=total_pages, current_page=page)


@app.route('/update/<string:user_id>', methods=['POST'])
def update(user_id):
    # Retrieve form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = int(request.form['age'])

    # Update user in the collection
    collection.update_one({'_id': ObjectId(user_id)}, {'$set': {
                          'first_name_db': first_name, 'last_name_db': last_name, 'age_db': age}})

    # Redirect back to the current page
    return redirect(request.referrer)


@app.route('/delete/<string:user_id>')
def delete(user_id):

    # Delete user from the collection
    collection.delete_one({'_id': ObjectId(user_id)})

    return redirect(request.referrer)


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
    app.run(host='0.0.0.0', port=5000, debug=True)
