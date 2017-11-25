from enum import Enum, auto


class Environment(Enum):

    TEST = auto()
    NP = auto()
    PR = auto()

    @staticmethod
    def values():
        return tuple([name for name in Environment.__members__.keys()])

