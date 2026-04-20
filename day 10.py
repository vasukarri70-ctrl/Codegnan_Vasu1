'''prime_num = int(input("Enter a number: "))
count = 0
for j in range(1,prime_num+1):
    print(j)
    if prime_num % j == 0:
       count += 1
       print(count)
if count == 2:
    print(f"{prime_num} is a prime number")
else:
    print(f"{prime_num} is not a prime number")
    

for an in range (2,100):
     count = 0
     for j in range(1, an+1):
        if an % j == 0:
            count +=1
     if count ==2:
         print (f"{an} is a prime number")
     else:
        print(f"{an} is not a prime number")
        
s = [1057,197,9,6,86,17673]
for an in s:
    count = 0
    for j in range(1,an+1):
        if an % j == 0:
            count +=1
    if count == 2:
       print(f"{an} is a prime")
    else:
        print (f"{an} is not a prime")

any = [2,356,8,6,3,2,8]
empty_ = []
for j in any:
    if j not in empty_:
        empty_.append(j)
print(empty_)

'''
so = int(input("enter any number"))
length_  = len(str (so))
Amstr_ = 0
for j in str (so):
    amstr_ += int(j) ** length_
    print(amstr_)
if amstr_ == so:
    print(f" {so} is amstrong num")
else:
    print(f" {so} is not an amstrong num")
    
    
