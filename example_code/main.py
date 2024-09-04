'''
Programmentwurf von:
https://www.youtube.com/watch?v=axi4PlzTnek
'''

from teacher import Teacher
from student import Student


#Client
def main():
    teacher = Teacher("Sean Campbell","Creational Design Pattern") # TY an Sean Campbell
    teacherClone = teacher.clone()
    teacherClone.display()

    student = Student("John Doe", teacherClone)
    studentClone = student.clone()
    studentClone.display()

    teacherClone.set_course("Python Programming Course")
    studentClone.display()

if __name__ == "__main__":
    main()
