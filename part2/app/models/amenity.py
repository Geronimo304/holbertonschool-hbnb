import uuid
from datetime import datetime


class Amenity:
    """Amenity entity class."""

    def __init__(self, name: str, description: str = ""):
        self.id = str(uuid.uuid4())
        self.name = self._validate_name(name)
        self.description = description
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def _validate_name(self, name):
        if not name or len(name) > 50:
            raise ValueError("Name must be between 1 and 50 characters.")
        return name

    def edit_amenity(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<Amenity {self.name}>"
