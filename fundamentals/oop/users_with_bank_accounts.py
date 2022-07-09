class Bank_account:

    def __init__(self, int_rate=.02, balance=0):
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


class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = Bank_account()

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def user_balance(self):
        self.account.display_account_info

    def display_info(self):
        print(f"name: {self.first_name} {self.last_name}")
        print(f"email: {self.email}")
        print(f"age: {self.age}")
        print(f"member?: {self.is_rewards_member}")
        print(f"gold card points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member:
            print("You're already a member!")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points - amount < 0:
            print("You don't have the points for that!")
        else:
            self.gold_card_points -= amount


user1 = User("Bob", "Barker", "bbboy@email.com", 77)
user2 = User("Kelly", "Kapur", "kittykat003@email.com", 27)
user3 = User("Donald", "Duck", "mickeybbf@email.com", 50)
