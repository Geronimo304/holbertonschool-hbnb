from datetime import datetime
from app.models.base_model import BaseModel
import uuid
from app.models.place import Place 


class User(BaseModel):
    """User entity class."""


    def __init__(self, first_name: str, last_name: str, email: str, is_admin: bool = False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = [] # esto no se si va 
        self.validate() # que hace validate sino son los setters


    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not self.first_name or len(self.first_name) > 50:
            raise ValueError("El nombre es obligatorio y debe tener menos de 50 caracteres.")
    
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not self.last_name or len(self.last_name) > 50:
            raise ValueError("El apellido es obligatorio y debe tener menos de 50 caracteres.")

    @property
    def email(self):
        return self._email

    @email.setter 
    def email(self, value):
        if not self.email or "@" not in self.email:
            raise ValueError("El email es obligatorio y debe tener un formato válido.")
    

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        self.validate()
    
    def create_place(self, title, description, price, latitude, longitude):
        new_place = Place(title, description, price, latitude, longitude)
        self.places.append(new_place.id)
        new_place.owner = self.id

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} ({self.email})>"
