import copy
from abc import ABC,abstractmethod


class Document(ABC):
    def __init__(self,type):
        self._type = type
    
    @abstractmethod
    def clone(self):
        pass
    
    def get_type(self):
        return self._type

    def set_type(self, type:str):
        self._type = type

    def __str__(self):
        return f"Document Type: {self._type}"


class Report(Document):
    def __init__(self, title, content, author):
        super().__init__("Report")
        self.title = title
        self.content = content
        self.author = author
        
    def clone(self):
        return copy.deepcopy(self)
    
    
class Contract(Document):
    def __init__(self, title, content, author):
        super().__init__("Contract")
        self.title = title
        self.content = content
        self.author = author

    def clone(self):
        return copy.deepcopy(self)

class Presentation(Document):
    def __init__(self, title, content, author):
        super().__init__("Presentation")
        self.title = title
        self.content = content
        self.author = author

    def clone(self):
        return copy.deepcopy(self)
    
