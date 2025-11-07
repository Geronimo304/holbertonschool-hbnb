from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place
from app import db

class Review(BaseModel):
    """Review entity class."""

    __tablename__ = 'reviews'

    _text = db.Column(db.Text, nullable=False)
    _rating = db.Column(db.Int, nullable=False)
    _user = db.Column(db.String(36), db.Foreignkey('users.id'), nullable=False)
    _place = db.Column(db.String(36), db.Foreignkey('places.id'), nullable=False)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if not text:
            raise ValueError("Text cannot be empty.")
        self._text = text

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not 1 <= value <= 5:
            raise ValueError("Rating must be between 1 and 5.")
        self._rating = value
    
    @property
    def user(self): 
        return self._user

    @user.setter
    def user(self, user):
        if not isinstance(user, User):
            raise TypeError("User must be a User instance.")
        return user

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, place):
        if not isinstance(place, Place):
            raise TypeError("Place must be a Place instance.")
        return place

    def edit_review(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key) and key not in ["id", "user", "place"]:
                setattr(self, key, value)
        self.save()

    def __repr__(self):
        return f"<Review {self.rating}/5 by {self.user.first_name} for {self.place.title}>"
