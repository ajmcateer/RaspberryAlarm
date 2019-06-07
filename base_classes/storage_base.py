from abc import ABC, abstractmethod


class StorageBase(ABC):

    @abstractmethod
    def __init__(self, connection):
        pass

    @abstractmethod
    def save(self, dic: dict):
        pass

    @abstractmethod
    def read(self):
        pass