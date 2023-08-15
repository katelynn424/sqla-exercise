"""Models for Blogly."""

import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """USER"""

    __tablename__ = "users"

    id = db.Column(db.Integer, 
                   primary_key= True,
                   autoincrement= True) 
    first_name = db.Column(db.Text,
                           nullable= False)
    last_name = db.Column(db.Text,
                         nullable= False)
    image_url = db.Column(db.Text,
                          nullable = False)
    
    @property
    def full_name(self):
        """Make and return full name of user"""

        return f"{self.first_name} {self.last_name}"
    
class Post(db.Model):
    """blog posts"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def friendly_date(self):
        """Return date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")