import SuperClase
from user import User

class Place(SuperClase):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        if not title or len(title) > 100:
            raise ValueError("El titulo es obligatorio y debe tener 100 caracteres máximo")
        self.title = title

        self.description = description

        if price is None or price < 0:
            raise ValueError("El precio es obligatorio y debe ser un valor valido")
        self.price = price

        if latitude < -90 or latitude > 90:
            raise ValueError("latitud debe ser mayor a -90 y menor a 90")
        self.latitude = latitude

        if longitude < -180 or longitude > 180:
            raise ValueError("longitud debe ser mayor a -180 y menor a 180")
        self.longitude = longitude

        if not isinstance(owner, user):
            raise ValueError("Debe asignarse un propietario")
        self.owner = owner