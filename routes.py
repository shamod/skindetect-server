from flask import Flask, request, jsonify
from app import app, db
from models import User

@app.route('/')
def home():
    return "Home"

@app.route('/login', methods=['POST'])
def login():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    
    msg = ""
    if not email or not password : 
        msg = {"status" : { "type" : "failure" ,   "message" : "Missing Data"}}
        return jsonify(msg)

    user = User.query.filter_by(email=email).first() 
    print(user.name)
    if user is None or not user.check_password(password) :
        msg = {"status" : { "type" : "failure" ,   "message" : "Username or password incorrect"}}
    else:
        msg = {"status" : { "type" : "success" ,
                             "message" : "You logged in"} , 
               "data" : {"user" : user.getJsonData() }
        }

    return jsonify(msg)

@app.route('/register', methods=['POST'])
def register():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    msg = ""
    if not name or not email or not password : 
        msg = {"status" : { "type" : "failure" ,   "message" : "missing data"}}
        return jsonify(msg)
    
    if User.query.filter_by(email=email).count() == 1 : 
        msg = {"status" : { "type" : "failure" ,   "message" : "email already taken"}}
        return jsonify(msg)

    u = User()
    u.name = name
    u.email = email
    u.set_password(password)

    db.session.add(u)
    db.session.commit()

    return jsonify({
        "type": "success",
        "message": "You have been regsitered",
    })