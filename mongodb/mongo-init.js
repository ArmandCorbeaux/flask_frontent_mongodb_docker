const dbName = 'users_database';
const collectionName = 'users';

// Connect to the MongoDB server
const conn = new Mongo();

// Get the database
const db = conn.getDB(dbName);

// Data to insert
const data = [
    {
        "__id__": "1",
        "last_name_db": "Michel",
        "first_name_db": "Paul",
        "age_db": 21
        },
        {
        "__id__": "2",
        "last_name_db": "Ayoub",
        "first_name_db": "Bastien",
        "age_db": 15
        },
        {
        "__id__": "3",
        "last_name_db": "Adrien",
        "first_name_db": "Antonin",
        "age_db": 14
        },
        {
        "__id__": "4",
        "last_name_db": "Baptiste",
        "first_name_db": "Louis",
        "age_db": 45
        },
        {
        "__id__": "5",
        "last_name_db": "Pablo",
        "first_name_db": "Abel",
        "age_db": 62
        },
        {
        "__id__": "6",
        "last_name_db": "Pierre",
        "first_name_db": "Quentin",
        "age_db": 22
        },
        {
        "__id__": "7",
        "last_name_db": "Leonard",
        "first_name_db": "Martin",
        "age_db": 22
        },
        {
        "__id__": "8",
        "last_name_db": "Gaspard",
        "first_name_db": "Benjamin",
        "age_db": 51
        },
        {
        "__id__": "9",
        "last_name_db": "Antonin",
        "first_name_db": "Mathias",
        "age_db": 18
        },
        {
        "__id__": "10",
        "last_name_db": "Romeo",
        "first_name_db": "Gaspard",
        "age_db": 30
        },
        {
        "__id__": "11",
        "last_name_db": "Elio",
        "first_name_db": "Ayden",
        "age_db": 34
        },
        {
        "__id__": "12",
        "last_name_db": "Léon",
        "first_name_db": "Daniel",
        "age_db": 38
        },
        {
        "__id__": "13",
        "last_name_db": "Marceau",
        "first_name_db": "Mathias",
        "age_db": 41
        }
];

