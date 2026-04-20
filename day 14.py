
'''Recursion is a programming technique where a function calls itself either directly or
indirectly to solve a problem by breaking it into smaller, simpler subproblems.
Recursion is especially useful for problems that can be divided into identical small tasks such
as mathematical calculations, tree traversals or divide-and-conquer algorithms


def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("Enter 4 digit PIN: ")
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print("Welcome to the ATM")
            return True
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print(f" Invalid PIN.Attempts left: {self.remaining_attempts}")
            else:
                print("Card blocked. please contact customer care")
                return false


any = "python is a language"
Vowel_list = []
COn_list = []
def Vowel_con(any,Vowel_list,Consonets_list):
    for j in any:
        if j in "AEIOUaeiou":
            Vowel_list.append(j)
        else:
            COn_list.append(j)
    print(f"{Vowel_list} these are all vowel in the string")
Vowel_con(any,Vowel_list,COn_list)

ICICI_saikumar_ac_details = {
    "Name": "saikumar",
    "ATM PIN": "0066",
    "balance": 10000
}

print("Welcome to ICICI ATM")
print("Please insert your ATM card")

ICICI_user_pin = input("Please enter the 4 digit ATM PIN: ")

# PIN validation
if len(ICICI_user_pin) == 4:
    if ICICI_user_pin == ICICI_vasu_ac_details["ATM PIN"]:
        print("PIN is correct")

        user_choice = int(input("Enter:\n1. Withdraw\n2. Deposit\n"))

        # ✅ Withdraw
        if user_choice == 1:
            money_w = int(input("Enter money you want to withdraw: "))

            if money_w <= ICICI_vasu_ac_details["balance"]:
                ICICI_saikumar_ac_details["balance"] -= money_w
                print("Transaction successful")
                print("Remaining balance:", ICICI_vasu_ac_details["balance"])
            else:
                print("Insufficient balance")

        # ✅ Deposit
        elif user_choice == 2:
            deposit_m = int(input("Enter money you want to deposit: "))

            # condition from your image code
            if deposit_m % 100 == 0 and deposit_m >= 500:
                ICICI_vasu_ac_details["balance"] += deposit_m
                print(f"You have deposited {deposit_m}")
                print("Total balance:", ICICI_vasu_ac_details["balance"])
            else:
                print("Invalid deposit amount (minimum 500 and multiples of 100 only)")

        # ✅ Invalid choice
        else:
            print("Invalid option selected")

    else:
        print("You have entered an invalid PIN")

else:
    print("Please enter a valid 4-digit PIN")
'''
