from models.base_model import BaseModel
from user import User

class Place(BaseModel):
    """Place entity class."""


    def __init__(self, title: str, description: str, price: float, latitude: float, longitude: float, owner: User):
        super().__init__()  # hereda id, created_at, updated_at
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def __repr__(self):
        return f"<Place {self.title} - Ubicación: {self.latitude}, {self.longitude}>"
