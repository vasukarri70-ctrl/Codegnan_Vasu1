'''
Encapsulation
----------------
--> The principle of bunding data (Attributes) and methods that
operate on that data into a single unit, which is a class
'''
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
















              
