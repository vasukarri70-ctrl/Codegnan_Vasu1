'''oop's
------
--> object-oreinted language (oop) is a style of programming where we model
    real-world things as objects that contain both data and functions()
-->reusable of code
-->and also scalable

class
-----
--> class is a blue-print or template that define what kind of data behavoiur
    a certain type of object will have

object
------
--> instance of class or an object is a real instance created from a class
    is the actual thing that exists in memory while the program run



Attributes
----------
-->these are variables that store data related to a class or object
'''

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 60
    def drive(self):
        self.speed = 60
        print(f"The {self.brand} {self.model} is now driving at {self.speed} km/h.")

