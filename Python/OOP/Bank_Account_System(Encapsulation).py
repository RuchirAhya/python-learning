class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        return self.__balance


acc = BankAccount(1000000000)

acc.deposit(5000000)
acc.withdraw(2000000000)

print("Balance =", acc.check_balance())