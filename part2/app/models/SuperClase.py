import uuid
from datetime import datetime

class SuperClass:
    def __init__(self):
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now()
        self.__update_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
