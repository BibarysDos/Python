class BankAccount:

    def __init__(self):
        self.current = None
        self.current: int
        self.username = None
        self.check_password = None
        self.password = None
        self.surname = None
        self.name = None
        self.balance = 0

    def create_account(self):
        self.name = input("Enter your name: ")
        self.surname = input("Enter your surname: ")
        self.password = input("Create password: ")
        self.check_password = input("Enter your password again: ")
        if self.password != self.check_password:
            print("Password not same")
            exit()
        else:
            pass

#         self.current = int(input('''Choose one of the currency
# 1.KZT
# 2.RUB
# 3.USD
# 4.EUR
# '''))
#         if self.current == 1:
#             return self.current == "KZT"
#         elif self.current == 2:
#             return self.current == "RUB"
#         elif self.current == 3:
#             return self.current == "USD"
#         elif self.current == 4:
#             return self.current == "EUR"
#         else:
#             print("Mistake")

        self.username = self.surname.lower() + self.name.lower()
        return f"Thank you {self.surname.title()} {self.name.title()} for creating account. " \
               f"\nYour username = {self.username}\n" \
               f"Your password = {self.password}\n" \
               # f"You choose {self.current} currency"

    def deposit(self):
        print(f"Your balance now {self.balance}")
        self.balance += int(input("How much you want deposit: "))
        return f"Thank you for depositing" \
               f"\nNow in your balance = {self.balance}"

    def withdraw(self):
        print(f"Your balance now {self.balance}")
        self.balance -= int(input("How much you want withdraw: "))
        return f"Thank you for withdrawing" \
               f"\nNow in your balance = {self.balance}"

    def __repr__(self):
        return f"{self.username} {self.password}"



data = []
acc = BankAccount()
print("Welcome our Bank")
while True:
    print('''
Chose what you want:
1.Create Account
2.Deposit
3.Withdraw
0.Exit''')
    command = int(input())

    if command == 1:
        print(acc.create_account())
        data.append(acc)
        print(data)

    if command == 2:
        print(acc.deposit())

    if command == 3:
        print(acc.withdraw())

    if command == 0:
        exit()


