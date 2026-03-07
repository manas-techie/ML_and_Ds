# Class : is the blueprint or templete for creating object.It define the structure and behaviour that the object will have
# object: is  a instance of class. it is a concrete entity created from the blue print 

class Car:
    pass  ## pass mean the class is empty for now 

car1 = Car()
car2 = Car()

print(type(car1))


# Constructor __init__
#__init__ method is special method automatically called when a new object created
# self parameter refer to the specific object being created

class Bike: 
    #constructor
    def __init__(self, make, model):
        self.make = make
        self.model  = model

# creating object with initial value
my_bike = Bike("honda", "X23")
print(f"I drive a {my_bike.make} {my_bike.model}")




### Instance Variables: variables define inside __inti__ using self . They are unique to each object 
### Class Variable: variables declare inside the class body . They are shared accross all object of the class

class Employee:
    ##class Varibale
    company_name = "TechGroup"

    def __init__(self,name):
        # instancce variable
        self.name = name

emp1 = Employee("Alice")
emp2 = Employee("Jhon")

print(emp1.company_name)
print(emp2.company_name)
print(emp1.name)


##method

# Methods are simply functions defined inside a class that describe the behaviors of an object.

# Instance Methods: Take self as the first parameter. They access and modify instance variables.

# Class Methods: Take cls as the first parameter and use the @classmethod decorator. They access and modify class variables.

# Static Methods: Do not take self or cls. They use the @staticmethod decorator and behave like normal functions grouped inside a class for logical organization.

class MathStudent:
    school = "High School"

    def __init__(self,name, score):
        self.name = name
        self.score = score

    # 1. Instance Method
    def get_grade(self):
        print(f"grade: {self.score}")
    
    # 2. class method 
    @classmethod
    def changeSchool(cls, newSchool):
         cls.school =newSchool

    # 3 . Static method
    @staticmethod
    def is_passing(score):
        return score >= 50
    

student = MathStudent("Manas Sidh", 90)

student.get_grade()
MathStudent.changeSchool("University")
print(MathStudent.is_passing(90))




## Inheritance: Inheritance allow a new class(child/subclass) to take on the method of an existing class (parent/superclass)

#single Inheritance

class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal): # Dog inherits from Animal
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.eat()  # Inherited method
my_dog.bark() # Own method


#multiple inheritance
class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Duck(Flyer, Swimmer): # Inherits from both
    pass

donald = Duck()
donald.fly()
donald.swim()


## Method Overloading

# If a child class provides a specific implementation of a method that is already defined in it's parent class , it is called method overriding

class Bird:
    def speak(self):
        print("chip chip")

class Crow(Bird):
    def speak(self):
        print("caw caw")

bird = Bird()
bird.speak()

crow = Crow()
crow.speak()


## Encapsulation

# Encapsulation is the bundling of data and methods within a class, and restricting direct access to some of the object's components to prevent accidental modification. Python uses underscores to denote access levels by convention.

# Public: name (Accessible from anywhere)

# Protected: _name (Accessible within the class and its subclasses - by convention)

# Private: __name (Accessible only within the class itself via name mangling)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public
        self._bank_type = "Checking" # Protected
        self.__balance = balance # Private

    # Public method to access private data safely (Getter)
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
print(account.owner)               # Works fine
print(account._bank_type)          # Works, but shouldn't be touched directly
# print(account.__balance)         # ERROR: AttributeError
print(account.get_balance())       # Correct way to access



## Polymorphism

# Polymorphism means "many forms." In Python, it allows different classes to have methods with the same name, and you can call that method without knowing the exact class type of the object

class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

# A function that demonstrates polymorphism
def make_animal_sound(animal):
    print(animal.sound())

cat = Cat()
cow = Cow()

make_animal_sound(cat) # Output: Meow
make_animal_sound(cow) # Output: Moo


## Magic/Dunder Method
# "Dunder" stands for double underscore
# __init__ => constructor
# __str__ => return a detailed string reprensentation for user
# __repr_ => return a details string reprensentation for devloper or debugging
# __len__ => Defines behaviour for the built in len() function


class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"
    
    def __repr__(self):
        return f"(title={self.title}, pages={self.pages})"
    def __len__(self):
        return self.pages


my_book = Book("Python 101", 350)

print(my_book)          # Uses __str__ -> Book: 'Python 101'
print(repr(my_book))    # Uses __repr__ -> (title='Python 101', pages=350)
print(len(my_book))     # Uses __len__ -> 350
