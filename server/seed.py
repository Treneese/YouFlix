#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker
from flask_bcrypt import Bcrypt

# Local imports
from server.config import app
from server.models import db, User

if __name__ == '__main__':
    fake = Faker()
    bcrypt = Bcrypt(app)
    with app.app_context():
        print("Starting seed...")
        db.drop_all()
        db.create_all()

        # Seed code goes here!
        user1 = User(username='user1', _password_hash=bcrypt.generate_password_hash('password1').decode('utf-8'))
        user2 = User(username='user2', _password_hash=bcrypt.generate_password_hash('password2').decode('utf-8'))

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
