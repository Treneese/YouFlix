#!/usr/bin/env python3

from flask import request, session, jsonify
from flask_bcrypt import Bcrypt
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_migrate import Migrate
from server.config import app, db, bcrypt, api, CORS
from server.models import User  # Use relative import

# Define your routes
class ClearSession(Resource):
    def delete(self):
        session.clear()
        return '', 204

class Signup(Resource):
    def post(self):
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            if User.query.filter_by(username=username).first():
                return {'message': 'User already exists'}, 400
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, _password_hash=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return new_user.to_dict(), 201
        except Exception as e:
            return {'message': str(e)}, 500

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        print(f"Session user_id: {user_id}")
        if user_id:
            user = User.query.get(user_id)
            if user:
                return user.to_dict()
            return {'message': 'User not found'}, 404
        return {'message': '401: Not Authorized'}, 401

class Login(Resource):
    def post(self):
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            user = User.query.filter_by(username=username).first()
            if not user:
                return {'message': 'User does not exist'}, 400
            if not bcrypt.check_password_hash(user._password_hash, password):
                return {'message': 'Incorrect password'}, 400
            session['user_id'] = user.id
            session.modified = True
            print(f"Session set: {session['user_id']}")
            return user.to_dict()
        except Exception as e:
            return {'message': str(e)}, 500

class Logout(Resource):
    def delete(self):
        session.clear()
        return '', 204

class UpdateAvatar(Resource):
    def patch(self):
        user_id = session.get('user_id')
        if not user_id:
            return {'message': '401: Not Authorized'}, 401
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        avatar_url = request.json.get('avatar_url')
        if avatar_url:
            user.avatar_url = avatar_url
            db.session.commit()
            return user.to_dict(), 200
        return {'message': 'No avatar URL provided'}, 400

class UpdateUsername(Resource):
    def patch(self):
        user_id = session.get('user_id')
        if not user_id:
            return {'message': '401: Not Authorized'}, 401
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        username = request.json.get('username')
        if username:
            user.username = username
            db.session.commit()
            return user.to_dict(), 200
        return {'message': 'No username provided'}, 400

api.add_resource(ClearSession, '/clear_session')
api.add_resource(Signup, '/signup')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(UpdateAvatar, '/update_avatar')
api.add_resource(UpdateUsername, '/update_username')

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
