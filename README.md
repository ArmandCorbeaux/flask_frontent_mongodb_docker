<center>
# A simple Flask CRUD application to manage a MongoDB Database in a docker container
</center>

## TO EXPLAIN :
It was at the beginning a simple project to discover :
- Flask CRUD functions
- Create a Docker container with a persistent volume
- Create a dockerfile for the flask app

But I've decided to add features, as a html frontend for Flask to immedialety see the results of the CRUD operations.

>There's also a set of datas which are uploaded into the demo database (in the MongoDB container) to test the functionalities of the frontend.

I've decided to implement a UI and improve it in a KISS way :
- **As user, I want to have immediately an overall view :** that's why the 'user database' entries are display 8 per 8
- **As user, I want to see immediately the results of my operations :** that's why the frontend goes or stays at the right page
- **As user, I want to understand immediately what kind of operations I can do :** that's why the UI is splitted and buttons have overlays effect

## WHAT IS PERFORMED?
- A docker container is build to host and launch the *Flask* app.
>I've decided to build a specific container based on Debian Bookworm, which is updated and where all the needed python librabries are installed in a virtual environment, then the Flask app is launched.
- The *MongoDB* container has persistent volumes. It will create 2 folders in the folder where you launch the docker-compose : data and configdb
>At the initial launch, the demo database set is injected
- A *mongo-express* container is launched to check the integrity of the databse after operations
-
## HOW TO RUN IT
**Prerequisite:**
- Have Docker installed on your OS : [https://www.docker.com/]()

**Clone the repository :**
```bash
git clone https://github.com/ArmandCorbeaux/flask_mongodb.git
```

**Launch it :**
```bash
docker-compose up -d
```

**Access it with his url in your browser:**
```
localhost:5000
```

## WHAT I WANT TO TEST, ADD OR IMPROVE?
- Have a 'password' column and features of encryption
- Change the code to manage the current version in the .env file
- Have a cleaner code