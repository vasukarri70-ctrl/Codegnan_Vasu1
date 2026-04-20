'''
if statement  ---> this (if statement) is used to check any condition,
if the condition becomes true then it will enter into inside the (if statement)
if-else statement
if-elif-else statement

student_att = int(input("enter attendeb=nce"))
if student_att >= 75 and student_att <= 100:
    print("you are eligible to write exam")
elif student_att < 75 and student_att > 0:
    print("you are ineligible")
else:
    print("percentage should be atleast greater than zero")


total_amt = int(input("enter the total shopping money"))
if total_amt >= 149:
    print("no delivery cost")
else:
    print(f"  u r having {total_amt - 149} more  to your cart ")


if elif else statement (if + else)--- in the elif part ,i can put more conditions 

bill_input = int(input("enter bill amt:"))
if bill_input >= 1000 and bill_input < 2000:
    print("you get 10% discount")
elif bill_input >= 2000 and bill_input < 2500:
    print("you get 20% discount")
elif bill_input >= 2500:
    print("you got vip subscription")


num_1 = int(input("enter  1st number"))
num_2 = int(input("enter  2nd number"))
user_choice = input("enter your choice")
if user_choice == "+":
    print(f"{num_1 + num_2}")
elif user_choice == "-":
    print(f"{num_1 - num_2}")



num_1 = int(input("enter  1st number"))
num_2 = int(input("enter  2nd number"))
user_choice = input("enter your choice\n 1.add \n 2.sub\n 3.mul\n 4.div\n")
if user_choice == "1":
    print(f"{num_1 + num_2}")
elif user_choice == "2":
    print(f"{num_1 - num_2}")
elif user_choice == "3":
    print(f"{num_1 * num_2}")
else:
    print(f"{num_1 / num_2}")



user_input = int(input("enter any digit"))
if user_input > 0:
    print("positive")
elif user_input < 0:
    print("negative")
else:
    print("zero")

'''






















