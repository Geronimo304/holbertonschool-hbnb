#!/usr/bin/python3
"""
BaseModel module
Define all common attributes and methods for other models
"""

from datetime import datetime
import uuid


class BaseModel:
    def __init__(self):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid.uuid4()) # Identificador único
        self.created_at = datetime.utcnow() # Fecha de creación
        self.updated_at = datetime.utcnow() # Fecha de última actualización

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Return a dictionary representation of the instance."""

        dictionary = self.__dict__.copy()
        # Convert datetime objects to ISO format strings
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['__class__'] = self.__class__.__name__
        return dictionary

    def __repr__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
