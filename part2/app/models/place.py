import uuid
from datetime import datetime
from user import User


class Place:
    """ Modulo Place """


    def __init__(self, title: str, description: str, price: float, latitude: float, longitude: float, owner: User):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<Place {self.title} - Ubicación: {self.latitude}, {self.longitude}>"
