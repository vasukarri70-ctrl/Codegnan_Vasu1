'''
string ---> string is a collection of char ,with represter
by " "or '' and we can access the using indexing (string slicing.
this also immutable, where i could not able to modify on that particular vari...''' 

any = 'python programming'
print(any[6])
so = any.replace("python","java")
print(any)
print(so)


'''len()---> len() method is used to get char present in the string
or find the length of string'''

a_day =("i'm Vasu from jagadamba, have 3+ years exp as ")
print(f"my name is {a_day[4:9]}")
print (f"i'm name Vasu from{a_day[1:39]}")

#reverse
day = 'vasu'
print(day[::-1])

#integer convrt the strings, if the contain only integers valus ....
some = "123"
num = int(some)
print(type(num))

#note [methods of string
#----------
#split()--->remove space, and the is in the list[]it will give seperated thing in each index

#syntax----->variable_name.split("substring")
#lower()--->this is used to all convert into lower case

some ="python is a programming language"
print(some.split(" "))

some = "python is a programming language"
print(some.split("programming"))


some = "python is a programming language"
print(some.lower())


some = "python is a programming language"
print(some.upper())
'''
upper()--->

replace()--->this is used to replace old str with the new str
syntax---> variable_name.replace("old string","new string")

some = "python is a programming language"
print(Some.replace("programming ","nrml"))'''


some = "python is a programming language"
if "pythn" in some:
    print("yes")
else:
    print("No")
