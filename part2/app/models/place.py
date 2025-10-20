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
        self.reviews = []     # lista de reviews asociadas
        self.amenities = []   # lista de amenities asociadas
        owner.add_place(self)  # agrega este place al usuario automáticamente
   
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

     def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
    
    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)
    
    def __repr__(self):
        return f"<Place {self.title} - Ubicación: {self.latitude}, {self.longitude}>"
