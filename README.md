# flask_mongodb

*That's a basic CRUD flask app linked with a MongoDB database*
---
IMPROVEMENTS TO PERFORM : flask app
---

WHAT IS DONE?
- Build a docker container from debian:bookworm base and install needed dependencies for flask server
- Pull and configure mongodb and mongo-express, then launch everything

**FIRST :**
-Ensure you to have docker installed

**SECOND :**
-Launch in terminal with:
```bash
docker-compose up -d
```

Stuffs can be accessed at these url :
[localhost:5000]() : CRUD flask app
[localhost:8081]() : mongo-express

-----
**MORE INFORMATIONS :**
- mongo-init.js gives datas to populate mongodb
- datas from mongodb are stored on your drive in the 'data' folder
