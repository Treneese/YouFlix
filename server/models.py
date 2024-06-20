from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from server.config import db, bcrypt 
import validators

class Show(db.Model, SerializerMixin):
    __tablename__ = "shows"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    summary = db.Column(db.Text)
    category = db.Column(db.String)
    subCategory = db.Column(db.String)

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
    
class Episode(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    summary = db.Column(db.Text)
    video = db.Column(db.String)
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'), nullable=False)

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
