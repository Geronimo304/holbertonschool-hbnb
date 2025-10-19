from datetime import datetime
import uuid

class User:
    """Representa un user"""

    def __init__(self, first_name: str, last_name: str, email: str, is_admin: bool = False):
        self.id = str(uuid.uuid4())  # identificador unico
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.validate()

        # Validar datos básicos
        self.validate()

    def validate(self):
        if not self.first_name or len(self.first_name) > 50:
            raise ValueError("El nombre es obligatorio y debe tener menos de 50 caracteres.")

        if not self.last_name or len(self.last_name) > 50:
            raise ValueError("El apellido es obligatorio y debe tener menos de 50 caracteres.")

        if not self.email or "@" not in self.email:
            raise ValueError("El email es obligatorio y debe tener un formato válido.")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = "Usuario actualizado"
        self.validate()

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} ({self.email})>"
