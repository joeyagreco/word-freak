from abc import abstractmethod, ABC


class Parser(ABC):

    @classmethod
    @abstractmethod
    def getWordFrequency(cls, pathToFile: str) -> dict[str, int]:
        ...
