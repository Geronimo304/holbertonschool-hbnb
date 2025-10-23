from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity entity class."""


    def __init__(self, name: str):
        super().__init__()  # Hereda id, created_at, updated_at
        self.name = self._validate_name(name)

    def _validate_name(self, name):
        if not name or len(name) > 50:
            raise ValueError("Name must be between 1 and 50 characters.")
        return name

    def edit_amenity(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)
        self.save()  # Actualiza updated_at

    def __repr__(self):
        return f"<Amenity {self.name}>"
