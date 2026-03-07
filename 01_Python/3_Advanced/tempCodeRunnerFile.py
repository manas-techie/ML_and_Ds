from datetime import datetime

def add_created_at(cls):
    cls.created_at = datetime.now()
    return cls

@add_created_at
class MyClass: 
    def __init__(self, value):
        self.value = value

my_class = MyClass(20)
print(my_class.value)
print(my_class.created_at)