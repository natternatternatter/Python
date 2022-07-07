class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

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
user1.enroll()

user2 = User("Kelly", "Kapur", "kittykat003@email.com", 27)
user3 = User("Donald", "Duck", "mickeybbf@email.com", 50)

user1.spend_points(50)
user2.enroll()
user2.spend_points(80)

user1.display_info()
user2.display_info()
user3.display_info()

user1.enroll()
user3.spend_points(40)
