class Animal:

    def talk(self):
        raise NotImplementedError("You need to choose specific animal")

class Dog(Animal):

    def talk(self):
        return "woof woof"

class Cat(Animal):
    
    def talk(self):
        return "meeoooow"

cat1 = Cat()
dog1 = Dog()

def say_hello(animal):
    return animal.talk()

print(say_hello(cat1))
print(say_hello(dog1))