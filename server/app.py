#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, jsonify, Flask
from flask_bcrypt import Bcrypt
from flask_restful import Resource, Api
from sqlalchemy.exc import IntegrityError
import logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Local imports
from server.config import app, db, bcrypt, migrate
from server.models import User

bcrypt = Bcrypt(app)
api = Api(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.before_request
def check_if_logged_in():
    open_access_list = [
        'signup',
        'login',
        'check_session'
    ]
    if request.endpoint not in open_access_list and not session.get('user_id'):
        return jsonify({'error': '401 Unauthorized'}), 401

import traceback

class Signup(Resource):
    def post(self):
        try:
            request_json = request.get_json()
            username = request_json.get('username')
            password = request_json.get('password')
            image_url = request_json.get('image_url')
            bio = request_json.get('bio')

            user = User(username=username, image_url=image_url, bio=bio)
            user.password_hash = password

            try:
                db.session.add(user)
                db.session.commit()
                session['user_id'] = user.id
                return user.to_dict(), 201
            except IntegrityError as e:
                logging.error(f"IntegrityError during signup: {e}")
                db.session.rollback()
                return {'error': '422 Unprocessable Entity'}, 422
        except Exception as e:
            logging.error(f"Error during signup: {e}")
            logging.error(traceback.format_exc())
            return {'error': '500 Internal Server Error'}, 500

@app.before_request
def check_if_logged_in():
    open_access_list = [
        'signup',
        'login',
        'check_session',
        'static', 
    ]
    if request.endpoint not in open_access_list and not session.get('user_id'):
        return jsonify({'error': '401 Unauthorized'}), 401


class CheckSession(Resource):
    def get(self):
        try:
            user_id = session.get('user_id')
            if user_id:
                user = User.query.get(user_id)
                return user.to_dict(), 200
            return {}, 401
        except Exception as e:
            logging.error(f"Error during check session: {e}")
            return {'error': '500 Internal Server Error'}, 500

class Login(Resource):
    def post(self):
        try:
            request_json = request.get_json()
            username = request_json.get('username')
            password = request_json.get('password')
            user = User.query.filter_by(username=username).first()

            if user and user.authenticate(password):
                session['user_id'] = user.id
                return user.to_dict(), 200
            return {'error': '401 Unauthorized'}, 401
        except Exception as e:
            logging.error(f"Error during login: {e}")
            return {'error': '500 Internal Server Error'}, 500

class Logout(Resource):
    def delete(self):
        try:
            session.pop('user_id', None)
            return {}, 204
        except Exception as e:
            logging.error(f"Error during logout: {e}")
            return {'error': '500 Internal Server Error'}, 500

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
