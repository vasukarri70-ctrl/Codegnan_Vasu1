''''

Operators
different type of operators
conditional statement-->if,elif,nested if
'''
'''operators-->An operator is a symbol that perform an
operator on one or more values (operands) and produces a result

operators are primarly used :
-->calculate values
-->compare values/ inputs
-->Make decisions
-->control the program flow

There are major seven categories of operators in python

-->Arithimetic Operators
-->Assignment operators
-->Comparision Operators
-->Membership Operators(in,not in)
-->Identify Operators  (is,is not)
-->Bitwise Operators  
-->Logical operators   (and,or,not)


#Arithmetic Operators -->Arithmetic Operators perform mathemetical operators

# + -->Addition,- -->Subtraction , * -->Multiplication, / -->   Division
# ** -->Exponent,% -->modulus ,// -->Integer Division

a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b) #returns the result in float values
print(a**b) #returns the exponential value

print(a%b) #Modulus division -->returns remainder
print(a//b) #Floor / Integer Division -->returns Quotient discards float

#f-string notation
num1 = int(input("Enter the first values:"))
num2 = float(input("Enter the second value:"))
result = (num1 + num2)*4
print("The result is",result) #standard notation

#f-string notation
print(f'The result is {result}')
print(f'The result of {num1} and {num2} is {result},{num1*num2}')


#Assignment Operators
#--> = Assign, += Addition Assignment ,
#-= -->Subtract Assignment,*=,/=,%=,//=,**=

#They are majorly used for code repetitions in application usage

a = 4
b = 3
a += 2 #--> a = a+2
print(a)
b += a 
print(b)
#in similar way check  for -=, *=, **=,/=, //=

b -= 3 # b =b*a
print(b)
print(f'The updated values of a and b are {a}')
#Logical Operators -->They check the/compare the memory location and validate we use
#(id)function it is different from == operator --> is, is not

a = [1,2,4]
b = [1,2,4]
print(a == b)
print(id(a))#returns the identify of an object
print(f'{a} and {b}')
a=7
b=8
b *= a # b =b*a
print(b)


#Relational or Compresions operators -->They always return the boolean
#values (True /False)

# == is equal to, !=not equal to
# < less than, > greater than, >= , <=

a = int(input("Enter a value:")) 
b = int(input("Enter the value:"))
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
              
#Membership operators -->They check for the existance of an object in a
#Collection --> in,not in

a = "codegnan"
print(type(a))
print('a' in a)
print('z' in 'vasu')
print('z' not in 'codegnan')

b = [12,6,3,4]
c =int(input("Enter the value"))
print(c)
print(c in b)
print(c not in b)


#Logical operators -->They are used to combine multiple conditions
#and,or,not

age = int(input("Enter the age:"))
vote_right =True
print(age>18 or vote_right)
print(not vote_right)


#Identity Operators -->They check the/compare the memory location and validate we use
#(id) fuction it is different from == operator --> is , is not

a = [1,2,4]
b = [1,2,4]
print(a == b)
print(id(a))#returns the identity of an object
print (id (b))
print (a is not b)

c = b
print(c) #assigning b to c
print(id(c)) #then b and c have same memory locations
print(c is b) #return true because b,c have the same memory locaton
'''
 
#bitwise operators -->Bitwise AND & ,Bitwise OR | perform bitwise operater
#we get the result (remeber thr binary conversation)
print(5&3)
print(bin(5)) #returns binary number

