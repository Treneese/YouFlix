#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_bcrypt import Bcrypt
from flask_restful import Resource

# Local imports
from config import app, db, api, bcrypt, migrate

# Add your model imports
from models import User

bcrypt = Bcrypt(app)

class ClearSession(Resource):
    pass

class Signup(Resource):
    pass

class CheckSession(Resource):
    pass

class Login(Resource):
    pass

class Logout(Resource):
    pass



# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)

