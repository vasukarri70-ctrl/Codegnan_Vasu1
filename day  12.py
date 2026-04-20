'''break---> this is used to exit from the loop, when we found the required value...
for j in range(1,10):
    print(j)
    if j == 5:
        break

lis_ = [1,2,3,4]
for n in lis_:
    print(n)
    if n == 1:
        break

continue--- this is used to skip that particular loop

for j in range(1,10):
    if j == 5:
        continue
    print(j)

lis_ = [1,2,3,4]
for n in lis_:
    if n == 3:
        continue
    print(n)

pass---this is called as space holder
incase any statement like
(if , for , else, elif...) this should complete, if not we will get indentation error to avoid this we
using pass




for j in range(1,10)
    pass

else -- for

for m in range(1,10):
    print(m)
else:
    print("else block")

while loop--- this a combination for and if statements, if we did not end the
loop in proper way it will run upto the memory space in the becomes empty
'''

user_in = int(input("Enter the limit: "))
num_1 = 0
num_2 = 1
print(num_1, num_2, end="")
for v in range(user_in+1):
    num_3 = num_1+ num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end="")


