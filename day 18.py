'''constructor(__init__)
---------------------
-->A constructor is a special method used to initialize object data
__init__()


class student:
    def __init__ (self, name, id):
       self.name = name
       self.id = id

    def display(self):
        print(self.name, self.id)
stu_1 = student("vasu", 123)
stu_1.display()

Access Specifiers
-----------------
1.public
SYNTAX -- name
we can use it anywhere in the program
2.protected
syntax -- _name
this is only for internal use

3.Private
syntax-- __name
this one is restricted

4.self
----
--> This keyword os instance variable and unique for each object

'''
class some:
    def __init__(self):
        self.public = "public"
        self.protected = "protected"
        self.private = "private"
any = some()
print(any.public)
print(any.protected)
print(any.private)
