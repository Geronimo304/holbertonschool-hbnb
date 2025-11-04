from models.base_model import BaseModel
from user import User
from place import Place

class Review(BaseModel):
    """Review entity class."""


    def __init__(self, text: str, rating: int, user: User, place: Place):
        super().__init__()
        self.text = self.text
        self.rating = self.rating
        self.user = self.user
        self.place = self.place
        place.add_review(self)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if not text:
            raise ValueError("Text cannot be empty.")
        return text
        
    @property
    def rating(self):
        return slef._rating

    @rating.setter
    def rating(self, rating):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5.")
        return rating
    
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
