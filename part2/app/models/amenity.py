from app.models.basemodel import BaseModel
import uuid

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()

        if not name or len(name) > 50:
            raise ValueError("El nombre es obligatorio y debe tener 50 caracteres máximo")
        self.name = name
