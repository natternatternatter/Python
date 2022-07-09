class Bank_account:

    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent funds, charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"balance: {self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


user1 = Bank_account(.1)
user1.deposit(300)
user1.display_account_info()
user2 = Bank_account(.3)
user2.deposit(500)
user2.withdraw(600)
user2.yield_interest()
user2.display_account_info()


user1.deposit(100).deposit(500).deposit(500).withdraw(
    600).yield_interest().display_account_info()
user2.deposit(500).deposit(100).withdraw(200).withdraw(200).withdraw(
    100).withdraw(200).yield_interest().display_account_info()
