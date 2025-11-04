from app.models.base_model import BaseModel
from app.models.user import User

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
   
    # valiadaciones automaticas
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number.")
        self._price = float(value)

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)) or not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        self._latitude = float(value)

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)) or not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        self._longitude = float(value)

    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def add_amenity(self, amenity):
        #if amenity not in self.amenities:
        #    self.amenities.append(amenity)
        pass
    
    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)
    
    def __repr__(self):
        return f"<Place {self.title} - Ubicación: {self.latitude}, {self.longitude}>"
