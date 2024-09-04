import copy
from person import Person

#ConcretePrototype1 
class Teacher(Person):
    
    def __init__(self, name: str, course: str):
        super().__init__(name)
        self._course = course
        
    def clone(self):
        return copy.copy(self)
    
    def display(self):
        print("Teacher was cloned: ")
        print("____________________")
        print(f"Name: {self._name}")
        print(f"Who teaches: {self._course}")

    def get_course(self):
        return self._course

    def set_course(self, course:str):
        self._course = course