'''
Regular expression
------------------
-->This regular expression or RegEx is a sequence of characters that forms a searching pattern.
--> To use this we have to import re, which will unlock the package

Functions
---------
1.findall
----------
--> by using this function, it will find all sequence in the string
syntax--> re.findall(metachar,variable_name)
2.search
--------
--> by using this function, it will only find first sequence in the string
syntax --> re.search("metachar",variable_name)

Metacharacters
--------------
--> Metacharacters are used to form searching pattern

1.[]
----
--> In this meta character we can search for [a-z],[A-Z],[0-9]

import re
any = "python is a language"
so = re.findall("a",any)
print(so)

import re
any = "There is a metachar here, and another metachar over there."
so = re.findall("[a-z]",any)
an = re.search("[a]",any)
print(so)
print(an)

import re
we = "hello"
the = re.findall("h....o",we)
thing = re.search("he..o",we)
print(the)
print(thing)

3.^
---
-> This is used to find the string is starting with the sequence or not

syntax --> re.finall("metachar",variable_name)

import re
how = "This is used to find the string is starting with sequence or not"
who = re.findall("^This is",how)
then = re.search("^This",how)
print(who)
print(then)

4.$ --> This is used to find string is string with the sequence or not
syntax--> re.findall("$",variable_name)

import re
out = "This is used to find string is ending with the sequence or not"
one = re.findall("sequence $",out)
two = re.search("This$", out)
print(one)
print(two)

5.* --> This meta character will form a searching pattern as it will take any zero or more character for (*)
syntax --> re.findall(".*",variable name)
import re
vasu = "This meta character will form a searching pattern as it will take any zero"
gk = re.findall("c.*",vasu)
nk = re.search("t.*",vasu)
print(gk)
print(nk)

6.+ --> this meta character will form a searching pattern as it will take any one or more character for (+)
syntax --> re.search(".+",variable_name)

import re
vasu = "this meta character will form a searching pattern as it will take any one or more characters for (+)"
gk = re.findall("an.+y",vasu)
nk = re.search("T. +",vasu)
print(gk)
print(nk)
'''
