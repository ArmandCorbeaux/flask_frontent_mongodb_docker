<center>


<img src=./assets/screenshot.png width= 500>

# A simple Flask CRUD application to manage a MongoDB database, with everything in a Docker container

</center>



## Introduction

This project was **originally a simple way to learn** about the Flask library, CRUD functions, Docker containers with persistent volumes, Dockerfiles, and Docker Compose.
However, I **decided to add features**, such as a HTML frontend for Flask to immediately see the results of CRUD operations.
I also **wanted to improve my knowledge in many ways**, including becoming more comfortable with the improvements to the Python environment in Debian Bookworm.

## The UI

I decided to **implement a UI** and **improve it in a KISS** (Keep It Simple, Stupid) **way**.
The goal was to provide users with an overview of the data in the database, as well as the ability to see the results of their operations immediately.
The UI is split into two sections: a list of all the entries in the database, and a form for adding or editing entries. The buttons in the UI have overlays to indicate what they do.

## The Docker containers

A Docker container is **built** to host and launch the Flask app. The MongoDB container has **persistent volumes**, which means that the data in the database will be saved even if the container is stopped or restarted.
A mongo-express container is also launched to **check the integrity** of the database after operations.

## How to run it

To run the application, you will need to have Docker installed on your computer.
And that's the only requirement.

Once you have Docker installed, you can clone the repository and launch the application with the following commands:

```bash
git clone https://github.com/ArmandCorbeaux/flask_mongodb.git
#launch the project
docker-compose up -d
```

The application will be available at http://localhost:5000.

2 folders will appear in the repository, which contain MongoDB datas.

## What I want to add and improve

I plan to add the following features and improvements to the application:

- Add a 'password' column to the database and manage encryption features.
~~- Change the code to manage the current version in the .env file.~~
- Have a cleaner code. # can make better
- Add comments to explain the code and the functions. # can make better too...
~~- Improve the UI.~~
- Add a warning popup with a choice for the delete button
- Add a password column and play with encryption library

**1.1 :**
- Cleaner UI / better use of the colors and non-colors
- More close to BootStrap CSS
- Minor changes to use .env in Dockerfile and more in docker-compose
- More comments in all the code to explain in a better way

## Conclusion

This project was a great way to learn about Flask, MongoDB, Docker, and other technologies. I am excited to continue working on it and adding new features.

I hope this is helpful! Let me know if you have any questions.