from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
import validators
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
    

    def __repr__(self):
        return f'User {self.username}, ID {self.id}'

    
class Show(db.Model, SerializerMixin):
    __tablename__ = 'shows'

    # Add serialization rules
    serialize_rules = ('-episodes.show',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    summary = db.Column(db.Text)
    category = db.Column(db.String)
    subCategory = db.Column(db.String)

    # Relationship to Episode
    episodes = db.relationship("Episode", back_populates="show", cascade="all, delete-orphan")

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError("Title cannot be empty")
        return title

    @validates('image')
    def validate_image(self, key, image):
        if not validators.url(image):
            raise ValueError("Image must be a valid URL")
        return image

    @validates('category')
    def validate_category(self, key, category):
        if not category:
            raise ValueError("Category cannot be empty")
        return category

    @validates('subCategory')
    def validate_subCategory(self, key, subCategory):
        valid_subcategories = ["shows", "movies", "kids"]
        if subCategory not in valid_subcategories:
            raise ValueError("Subcategory must be one of: shows, movies, kids")
        return subCategory

def __repr__(self):
    return f"<Show {self.title}>"

class Episode(db.Model, SerializerMixin):
    __tablename__ = "episodes"

    # Add serialization rules
    serialize_rules = ('-show.episodes',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    summary = db.Column(db.Text)
    video = db.Column(db.String)
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'), nullable=False)

    # Relationship to Show
    show = db.relationship("Show", back_populates="episodes")

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError("Title cannot be empty")
        return title

    @validates('summary')
    def validate_summary(self, key, summary):
        if not summary:
            raise ValueError("Summary cannot be empty")
        if len(summary) <= 5:
            raise ValueError("Summary must be more than 5 characters long")
        return summary

    @validates('video')
    def validate_video(self, key, video):
        if not video:
            raise ValueError("Video cannot be empty")
        if not video.startswith("https://www.youtube.com/embed/"):
            raise ValueError("Video must have a valid YouTube embed URL format")
        return video

    def __repr__(self):
        return f"<Episode {self.title}>"

    