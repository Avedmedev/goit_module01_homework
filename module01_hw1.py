from abc import ABC, abstractmethod
import pickle
import json


class SerializationInterface(ABC):
    @abstractmethod
    def read(self, filename):
        ...


    @abstractmethod
    def write(self, filename, some_data):
        ...


class JSONSerialization(SerializationInterface):
    def read(self, filename):
        with open(filename, "r") as fh:
            unpacked = json.load(fh)
        return unpacked

    def write(self, filename, some_data):
        with open(filename, "w") as fh:
            json.dump(some_data, fh)


class BINSerialization(SerializationInterface):
    def read(self, filename):
        with open(filename, "wb") as fh:
            unpacked = pickle.load(fh)
        return unpacked

    def write(self, filename, some_data):
        with open(filename, "wb") as fh:
            pickle.dump(some_data, fh)
