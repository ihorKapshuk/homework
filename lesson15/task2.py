class Dog:

    age_factor = 7

    def __init__(self, dog_age : int):
        self.dog_age = dog_age
    
    def human_age(self):
        return f"Dog age {self.dog_age} years in human equivalent : {self.dog_age * self.age_factor} years"

dog1 = Dog(5)
print(dog1.human_age())