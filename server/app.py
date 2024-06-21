#!/usr/bin/env python3

from flask import request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_restful import Resource
from config import app, db, api, bcrypt, migrate
from models import User

bcrypt = Bcrypt(app)

class ClearSession(Resource):
    def post(self):
        session.clear()
        return {}, 204

class Signup(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username is None or password is None:
            return {'message': 'Username and password are required'}, 400

        if User.query.filter_by(username=username).first():
            return {'message': 'User already exists'}, 400

        new_user = User(username=username)
        new_user.password_hash = password

        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id

        return {'id': new_user.id, 'username': new_user.username}, 201

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return {'message': 'Not logged in'}, 401

        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        return {'id': user.id, 'username': user.username}, 200

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.authenticate(password):
            session['user_id'] = user.id
            return {'id': user.id, 'username': user.username}, 200

        return {'message': 'Invalid credentials'}, 401

class Logout(Resource):
    def post(self):
        session.clear()
        return {}, 204

api.add_resource(ClearSession, '/clear_session')
api.add_resource(Signup, '/signup')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
