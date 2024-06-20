#!/usr/bin/env python3

# Standard library imports
from flask_cors import CORS
from flask import Flask


app = Flask(__name__)
CORS(app)
# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports

# Views go here!

from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

@app.route('/profiles', methods=['POST'])
def create_profile():
    data = request.json
    new_profile = Profile(name=data['name'], user_id=data['user_id'])
    db.session.add(new_profile)
    db.session.commit()
    return jsonify({'message': 'Profile created'}), 201

@app.route('/profiles/<int:id>', methods=['DELETE'])
def delete_profile(id):
    profile = Profile.query.get(id)
    if profile is None:
        return jsonify({'message': 'Profile not found'}), 404
    db.session.delete(profile)
    db.session.commit()
    return jsonify({'message': 'Profile deleted'}), 200

@app.route('/profiles/<int:id>', methods=['PATCH'])
def edit_profile(id):
    data = request.json
    profile = Profile.query.get(id)
    if profile is None:
        return jsonify({'message': 'Profile not found'}), 404
    profile.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Profile updated'}), 200

@app.route('/profiles/<int:id>', methods=['GET'])
def get_profile(id):
    profile = Profile.query.get(id)
    if profile is None:
        return jsonify({'message': 'Profile not found'}), 404
    return jsonify({'name': profile.name, 'user_id': profile.user_id}), 200

@app.route('/shows', methods=['GET'])
def search_shows():
    query = request.args.get('query')
    shows = Show.query.filter(Show.title.contains(query)).all()
    return jsonify([show.title for show in shows]), 200

@app.route('/profiles/<int:profile_id>/my_list', methods=['POST'])
def My_list(profile_id):
    data = request.json
    profile = Profile.query.get(profile_id)
    show = Show.query.get(data['show_id'])
    if profile and show:
        profile.my_list.append(show)
        db.session.commit()
        return jsonify({'message': 'Show added to My List'}), 200
    return jsonify({'message': 'Profile or Show not found'}), 404

@app.route('/profiles/<int:profile_id>/my_list/<int:show_id>', methods=['DELETE'])
def delete_favorite(profile_id, show_id):
    profile = Profile.query.get(profile_id)
    show = Show.query.get(show_id)
    if profile and show:
        profile.my_list.remove(show)
        db.session.commit()
        return jsonify({'message': 'Show removed from My List'}), 200
    return jsonify({'message': 'Profile or Show not found'}), 404



@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)