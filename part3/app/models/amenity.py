from app.models.base_model import BaseModel
from app import db

# review_amenity = db.Table(
#     'reviews',
#     db.Column('place_id', db.String(36), db.ForeignKey('places.id'), primary_key=True),
#     db.Column('amenity_id', db.String(36), db.ForeignKey('amenities.id'), primary_key=True)
# )


class Amenity(BaseModel):
    """Amenity entity class."""


    __tablename__ = 'amenities'

    _name = db.Column(db.String(30), nullable=False)

    # getters y setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, text):
        if not text or len(text) > 50:
            raise ValueError("Name must be between 1 and 50 characters.")
        self._name = text

    # Metodos
    def edit_amenity(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)
        self.save()  # Actualiza updated_at

    def __repr__(self):
        return f"<Amenity {self.name}>"
