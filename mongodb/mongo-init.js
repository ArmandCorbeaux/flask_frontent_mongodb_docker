db = db.getSiblingDB('users_database');

db.createCollection('users');

db.users.insertMany([
    { last_name_db: "Michel", first_name_db: "Paul", age_db: 21 },
    { last_name_db: "Ayoub", first_name_db: "Bastien", age_db: 15 },
    { last_name_db: "Adrien", first_name_db: "Antonin", age_db: 14 },
    { last_name_db: "Baptiste", first_name_db: "Louis", age_db: 45 },
    { last_name_db: "Pablo", first_name_db: "Abel", age_db: 62 },
    { last_name_db: "Pierre", first_name_db: "Quentin", age_db: 22 },
    { last_name_db: "Leonard", first_name_db: "Martin", age_db: 22 },
    { last_name_db: "Gaspard", first_name_db: "Benjamin", age_db: 51 },
    { last_name_db: "Antonin", first_name_db: "Mathias", age_db: 18 },
    { last_name_db: "Romeo", first_name_db: "Gaspard", age_db: 30 },
    { last_name_db: "Elio", first_name_db: "Ayden", age_db: 34 },
    { last_name_db: "Léon", first_name_db: "Daniel", age_db: 38 },
    { last_name_db: "Marceau", first_name_db: "Mathias", age_db: 41 }
]);