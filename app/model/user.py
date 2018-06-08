from .base_dto import JsonSerializable

class User(JsonSerializable):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.email = kwargs.get('email', None)
        self.password = kwargs.get('password', None)

    def json(self):
        json = {
            'id': self.id,
            'email': self.email,
            'password': self.password
        }
        return { k: json[ k ] for k in json.keys() if json[ k ] }

    @classmethod
    def from_json(cls, **kwargs):
        instance = cls()
        instance.id = kwargs.get('id', None)
        instance.email = kwargs.get('email', None)
        instance.password = kwargs.get('password', None)
        return instance