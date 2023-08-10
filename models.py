"""Models for Blogly."""
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
    last_name = db.Colum(db.Text,
                         nullable= False)
    image_url = db.Column(db.Text,
                          nullable = False)
    
    @property
    def full_name(self):
        """Make and return full name of user"""

        return f"{self.first_name} {self.last_name}"