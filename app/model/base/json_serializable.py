import abc

class JsonSerializable(abc.ABC):

    @abc.abstractmethod
    def json(self):
        pass