from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from server.config import db, bcrypt 
from config import db




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
        # Add image URL validation logic if required
        return image

    @validates('category')
    def validate_category(self, key, category):
        # Add category validation logic if required
        return category

    @validates('subCategory')
    def validate_subCategory(self, key, subCategory):
        # Add subCategory validation logic if required
        return subCategory

    def __repr__(self):
        return f"<Show {self.name}>"
    
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
        # Add summary validation logic if required
        return summary

    @validates('video')
    def validate_video(self, key, video):
        # Add video URL validation logic if required
        return video


    def __repr__(self):
        return f"<Episode {self.title}>"