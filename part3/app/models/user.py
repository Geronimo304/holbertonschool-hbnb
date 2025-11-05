from datetime import datetime
from app.models.base_model import BaseModel
from flask_bcrypt import bcrypt


class User(BaseModel):
    """User entity class."""


    def __init__(self, first_name: str, last_name: str, email: str, password: str, is_admin: bool = False):
        super().__init__()
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._is_admin = is_admin

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value or len(value) > 50:
            raise ValueError("El nombre es obligatorio y debe tener menos de 50 caracteres.")
        self._first_name = value
    
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value or len(value) > 50:
            raise ValueError("El apellido es obligatorio y debe tener menos de 50 caracteres.")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter 
    def email(self, value):
        if not value or "@" not in value:
            raise ValueError("El email es obligatorio y debe tener un formato válido.")
        self._email = value
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self.hash_password(new_password)

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self._password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        self.validate()

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} ({self.email})>"
