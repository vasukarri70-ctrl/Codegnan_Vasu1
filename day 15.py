#modules
'''
--> A module in a python is simply life that contain python code
    (functions, variable, classes)
--> To use modules, we have to use a keyword called import before
    the module

                    Types of modules
    #Userdefined modules
-->This is devoloped by the user or programmer inside a file of python code
    and used by called import with filename..

#syntax--> import(keyword) file_name
           file_name.functionality


#Example-1
import my_module
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(my_module.add(num1,num2))
      
#Example-2
import my_module
import check_prime
print(my_module.add(4,5))
num = int(input("Enter a num to check for prime:"))
if check_prime.prime_num(num)is True:
    print(f"{num}is a prime number")
else:
   print(f"{num}is not a prime number")

#Built-in or inbuilt

-->Already these comes with installation and they are ready to use in the program
-->This is devoloped by the devoloper

#Example1
import math
print(f"The value of 2 to the power 3 is{math.pow(2,3)}")
print(f"The square root of 25 is {math.sqrt(25)}")
'''


import pyttsx3
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
    
speak_text("Hello, I am your mentor how can i help you")























