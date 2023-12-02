class Person:

    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age

class Student(Person):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.mark = 0
    
    def add_hwork(self, content : str, teacher):
        teacher.hwork = content
    
    def check_mark(self):
        if self.mark > 0:
            return f"{self.name} have a good mark)))))))"
        else:
            return f"{self.name} have a bad mark(((((((("


class Teacher(Person):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.wage = 0
        self.hwork = ""
    
    def check_hwork(self, student):
        if self.hwork == "print('hello world')":
            student.mark += 1
            self.wage += 1
            self.hwork = ""
            return "HM is checked"
        else:
            return "There are no HW"
    
    def check_wage(self):
        if self.wage > 0:
            return f"{self.name} bank account is not empty"
        else:
            return f"{self.name} bank aacount is empty"


student1 = Student("Ihor", 20)
teacher1 = Teacher("Vasil", 49)

print(student1.check_mark())
print(teacher1.check_wage())
student1.add_hwork("print('hello world')", teacher1)
print(teacher1.check_hwork(student1))
print(teacher1.check_wage())
print(student1.check_mark())