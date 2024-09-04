from abc import ABC, abstractmethod


# Erstellen eine abstrakte Baseclass indem Person von ABC erbt
class Person(ABC):
    def __init__(self, name: str):
        self._name = name

    # Interface Methode - Muss in allen Unterklassen als Methode implementiert werden.
    @abstractmethod
    def clone(self):
        pass

    # Interface Methode - Muss in allen Unterklassen als Methode implementiert werden.
    @abstractmethod
    def display(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, name:str):
        self._name = name



