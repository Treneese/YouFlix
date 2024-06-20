from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, bcrypt

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    _password_hash = db.Column(db.String, nullable = False)

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        # utf-8 encoding is required in python 3
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    @classmethod
    def create_table(cls):
        """ Create new table for users """
        # SQL Here?
        # CURSOR.execute(sql)
        # CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table for Trains """
        # SQL Here?
        # CURSOR.execute(sql)
        # CONN.commit()

    def __repr__(self):
        return f'User {self.username}, ID {self.id}'