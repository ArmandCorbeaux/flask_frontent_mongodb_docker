#!/usr/bin/env python3
from flask import Flask, render_template, request, url_for, redirect
import subprocess as sp
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def load_stored_variables_in_env_file(VARENV:str):
    """load variables from .env file

    Arguments:
        VARENV -- searched env variable

    Returns:
        VARENV -- value for env variable
    """    
    load_dotenv()
    return os.getenv(VARENV)

ip_mongodb = load_stored_variables_in_env_file("ip_mongodb")
port_mongodb = load_stored_variables_in_env_file("password_mongodb")
username_mongodb = load_stored_variables_in_env_file("user_mongodb")
password_mongodb = load_stored_variables_in_env_file("password_mongodb")

app = Flask("UsersManagement")

client = MongoClient(ip_mongodb, port_mongodb,username=username_mongodb,password=password_mongodb)
db = client.users_database
users = db.users

@app.route("/")
def index():
    date = sp.getoutput("date /t")
    return render_template("index.html",date=date)

@app.route("/curd")
def insert_val():
    return render_template("curd.html")

@app.route("/read")
def read():
    cursor = users.find()
    for record in cursor:
        read_res = record["__id__", "first_name_db", "last_name_db", "age_db"]
        print(record)
    return render_template("response.html",res = read_res)

@app.route("/insert")
def insert():
    __id__ = record["__id__"]
    first_name_db = record["first_name_db"]
    last_name_db = record["last_name_db"]
    age_db = record["age_db"]
    myVal = { "__id__": __id__, "first_name_db": first_name_db, "last_name_db":last_name_db, "age_db":age_db }
    x = users.insert_one(myVal)
    return render_template("response.html", res = x)

@app.route("/delete")
def delete():
    __id__ = record["__id__"]
    myquery = { "id": __id__ }
    users.delete_one(myquery)
    x= "Record delete"
    return render_template("response.html", res = x)

@app.route("/update")
def update():
    __id__ = request.args.get["__id__"]
    new_first_name_db = request.args.get["first_name_db"]
    new_last_name_db = request.args.get["last_name_db"]
    new_age_db = request.args.get["age_db"]
    newvalues = { "$set": {"first_name_db": new_first_name_db, "last_name_db":new_last_name_db, "age_db": new_age_db }}
    users.update_one(myquery, newvalues)
    x = "Record updated"
    return render_template("response.html", res =x)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)