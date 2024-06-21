#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, session, make_response, jsonify
from flask_bcrypt import Bcrypt
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api, bcrypt, migrate

# Add your model imports
from models import User, Episode, Show

bcrypt = Bcrypt(app)

@app.before_request
def check_if_logged_in():
    open_access_list = [
        'signup',
        'login',
        'check_session'
    ]
    # if (request.endpoint) not in open_access_list and (not session.get('user_id')):
    #     return {'error': '401 Unauthorized'}, 401

# class ClearSession(Resource):
#     pass

class Signup(Resource):
    def post(self):
        request_json = request.get_json()
        username = request_json.get('username')
        password = request_json.get('password')
        image_url = request_json.get('image_url')
        bio = request_json.get('bio')
        user = User(
            username=username,
            image_url=image_url,
            bio=bio
        )
        # the setter will encrypt this
        user.password_hash = password
        try:
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return user.to_dict(), 201
        except IntegrityError:
            return {'error': '422 Unprocessable Entity'}, 422

class CheckSession(Resource):
    def get(self):
        user_id = session['user_id']
        if user_id:
            user = User.query.filter(User.id == user_id).first()
            return user.to_dict(), 200
        return {}, 401

class Login(Resource):
    def post(self):
        request_json = request.get_json()
        username = request_json.get('username')
        password = request_json.get('password')
        user = User.query.filter(User.username == username).first()
        if user:
            if user.authenticate(password):
                session['user_id'] = user.id
                return make_response(user.to_dict(), 200)
        else: 
            return make_response({'error': '401 Unauthorized'}, 401)

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {}, 204



# Views go here!


api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')

# @app.route('/show/<int:id>', methods=['GET'])
# def get_show(id):
#     show = Show.query.get(id)
#     if show is None:
#         return jsonify({"error": "Show not found"}), 404
#     return jsonify(show.to_dict())

# @app.route('/shows', methods=['GET'])
# def get_shows():
#     shows = Show.query.all()
#     return jsonify([{
#         "id": show.id, 
#         "title": show.title, 
#         "image": show.image
#     } for show in shows]), 200

@app.route('/shows', methods=['GET'])
def get_shows():
    subcategory = request.args.get('subCategory')
    
    if subcategory:
        shows = Show.query.filter_by(subCategory=subcategory).all()
    else:
        shows = Show.query.all()

    return jsonify([{
        "id": show.id,
        "title": show.title,
        "image": show.image
    } for show in shows]), 200

# @app.route('/show/<int:id>', methods=['GET'])
# def search_shows():
#     query = request.args.get('query')
#     shows = Show.query.filter(Show.title.contains(query)).all()
#     return jsonify([show.title for show in shows]), 200
# class Show(Resource):
#    def get_show(id):
#     show = Show.query.get(id)
#     if show is None:
#         return jsonify({"error": "Show not found"}), 404
#     return jsonify(show.to_dict())



# # @app.route('/shows', methods=['GET'])

#     def get_shows():
#         shows = Show.query.all()
#         return jsonify([{
#         "id": show.id, 
#         "name": show.name, 
#         "image": show.image
#     } for show in shows]), 200

@app.route('/show/<int:show_id>', methods=['GET'])
def get_show(show_id):
    show = Show.query.get(show_id)
    if show is None:
        return make_response(jsonify({"error": "Show not found"}), 404)
    return jsonify({
        "id": show.id,
        "title": show.title,
        "image": show.image,
        "summary": show.summary,
        "category": show.category,
        "subCategory": show.subCategory,
        "episodes": [{
            "id": episode.id,
            "title": episode.title,
            "summary": episode.summary,
            "video": episode.video
        } for episode in show.episodes]
    }), 200 


#     return response


@app.route('/')
def index():
    return "Index for Show/Episode/User API"


if __name__ == '__main__':
    app.run(port=5555, debug=True)