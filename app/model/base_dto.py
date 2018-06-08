import abc

class JsonSerializable( abc.ABC ):

    @abc.abstractmethod
    def json(self):
        pass

    @abc.abstractclassmethod
    def from_json(cls):
        pass