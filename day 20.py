'''
Encapsulation
----------------
--> The principle of bunding data (Attributes) and methods that
operate on that data into a single unit, which is a class

class bankac:
     def __init__(self, balance):
         self.__balance = balance

     def deposite(self, amount):
         self.__balance += amount

     def get_balance(self):
         return self.__balance

acc = bankac(15000)
acc.deposite(7000)
print(acc.get_balance())

inheritance
-----------
--> this allows a child class (sub class) to acquire the attributes and methods
    of a parent class (base class) this is called inheritance
1.single inheritance

2.multiple


class parent:
    def display(self):
        print("this is parent method")
class child(parent):
    def display(self):
        super().display()
        print("this is child method")
obj = child()
obj.display()

super()
------
--> this is used to call methods of the parent class from the child class


'''
class Father:
    def skill_1(self):
        print("Father: hard working")
class Mother:
    def skill_2(self):
        print("Mother: Cooking")
class Child(Father, Mother):
    def All_skills(self):
        print("Child: Coding")
ANy = Child()
ANy.skill_1()
ANy.skill_2()
ANy.All_skills()



              
