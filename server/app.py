#!/usr/bin/env python3

# Standard library imports
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app, db
from models import Profile, Show

# Local imports
from config import app, db

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-database-file.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Routes
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


# #@app.route('/shows', methods=['GET'])
# def get_shows():
#     shows = Show.query.all()
#     return jsonify([{"id": show.id, "name": show.name, "image": show.image} for show in shows]), 200

# @app.route('/shows', methods=['POST'])
# def create_show():
#     data = request.get_json()
#     new_show = Show(name=data['name'], image=data['image'])
#     db.session.add(new_show)
#     db.session.commit()
#     return jsonify({"id": new_show.id, "name": new_show.name, "image": new_show.image}), 201

# @app.route('/shows/<int:show_id>', methods=['DELETE'])
# def delete_show(show_id):
#     show = Show.query.get(show_id)
#     if show is None:
#         abort(404)
#     db.session.delete(show)
#     db.session.commit()
#     return '', 204

# if __name__ == '__main__':
#     app.run(debug=True)

# @app.route('/shows', methods=['GET'])
# def get_shows():
#     shows = Show.query.all()
#     return jsonify([{
#         "id": show.id, 
#         "name": show.name, 
#         "image": show.image
#     } for show in shows]), 200

# @app.route('/shows/<int:show_id>', methods=['GET'])
# def get_show(show_id):
#     show = Show.query.get(show_id)
#     if show is None:
#         abort(404)
#     return jsonify({
#         "id": show.id,
#         "name": show.name,
#         "image": show.image,
#         "video": show.video,
#         "summary": show.summary,
#         "category": show.category,
#         "subCategory": show.subCategory,
#         "episode": show.episode,
#         "episodeSummary": show.episodeSummary
#     }), 200

# @app.route('/shows', methods=['POST'])
# def create_show():
#     data = request.get_json()
#     new_show = Show(
#         name=data['name'], 
#         image=data['image'],
#         video=data.get('video'),
#         summary=data.get('summary'),
#         category=data.get('category'),
#         subCategory=data.get('subCategory'),
#         episode=data.get('episode'),
#         episodeSummary=data.get('episodeSummary')
#     )
#     db.session.add(new_show)
#     db.session.commit()
#     return jsonify({"id": new_show.id, "name": new_show.name, "image": new_show.image}), 201

# @app.route('/shows/<int:show_id>', methods=['DELETE'])
# def delete_show(show_id):
#     show = Show.query.get(show_id)
#     if show is None:
#         abort(404)
#     db.session.delete(show)
#     db.session.commit()
#     return '', 204

# if __name__ == '__main__':
#     app.run(debug=True)