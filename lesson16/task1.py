class Person:

    def __init__(self, name, surename):
        self.name = name
        self.surename = surename

class Student(Person):

    marks = 0

    def __init__(self, name, surename):
        super().__init__(name, surename)
    
    def do_task(self, content):
        return content
    
    def check_answer(self, answer):
        if answer == True:
            self.marks += 1
            return "Good boy"
        else:
            return "Try once more"

    def check_marks(self):
        if self.marks > 0:
            return "Good mark"
        else:
            return "Bad mark"

class Teacher(Person):

    wage = 0

    def __init__(self, name, surename):
        super().__init__(name, surename)
    
    def check_task(self, content):
        if content == "50$":
            self.wage += 1
            return True
        else:
            self.wage += 1
            return False
    
    def check_wage(self):
        if self.wage > 0:
            return "Good finance situation"
        else:
            return "Bad finance situation"

student1 = Student("Vasil", "Ivanenko")
teacher1 = Teacher("Petro", "Vasilenko")
print(student1.check_marks())
task = student1.do_task("50$")
print(teacher1.check_wage())
answer = teacher1.check_task(task)
print(teacher1.check_wage())
print(student1.check_answer(answer))
print(student1.check_marks())