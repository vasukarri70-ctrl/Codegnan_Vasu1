'''
functions()
---> this a block of code which is reuseable.
-->two types 1Bulit-in or In-bulid
             2.User define
Bulit-in or In-bulid
-->they comes with program and those are already defined...
eg..
---- print(), sum(), map().....

User define
-->  this is created by person who is developing or using for development
Note:
---> it's starts with keyword follwed by func name
---> and it has calling func...
systax:
        def fun-name(): parameters
           ......
           ........
           ........
           ........
        func_name() ..... arguments

'Even Number Using Functions'

a=int(input("enter the number:"))
def even(a):
   if a%2 == 0:
      print(f"{a} is even number")
   else:
      print(f"{a} is odd number")
even(a=2)


'Prime Numbers Using functions'

prime_num = 7
count = 0
def prime_check(num,k):
    for j in range (1,num+1):
        if num % j == 0:
            k += 1
    if k == 2:
        print("prime")
    else:
        print("not")
prime_check(prime_num,count)


a = [3,4]
b = [3,4]
c = b
print(id(c), id(b))
print(c is b)

required arguments
-----------------------------------------------------------------------
-->It should match the same number variables in calling the def

num = 9
num_2=10
def add (num,num_2):
    print(num)
add (num, num_2)
----------------------------------------------------------------
Default arguments

my_name="Vasu"
def sum_num(my_name):
    print(my_name)
sum_num(my_name="Vasu")
sum_num(my_name="Karri")
---------------------------------------------------------------
def even_check(num):
   if num %2==0 :
      print("even number")
   else:
      print("odd number")
   even_check_num
n = int(input("enter a number"))

def prime_num(num,count):
    for j in range(1,num+1):
        if num % j == 0:
            count+= 1
    if count == 2:
        print(f"{num} is a prime")
    else:
        print(f"{num} is not a prime")
prime_num(num=9,count=0)
prime_num(num = 47, count = 0)

----------------------------------------------------------------
Keywords arguments
---> above num = 47 is called key word arguments
def any(num,num_3,num_2):
    print(f"num= {num}, num_2={num_2},num_3={num_3}")
any(num_2=7, num=0, num_3 = 90)
---------------------------------------------------------------
def name(*Candidate_):
    print(Candidate_)
name("Teja","Sony","Sakheer")

