from xmlrpc.server import DocCGIXMLRPCRequestHandler


class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, Pet):
        self.first_name = first_name
        self.first_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet()

    def walk(self):
        print("Let's go for a walk.")
        self.pet.play()

    def feed(self):
        print("Here's some food.")
        self.pet.eat()

    def bathe(self):
        print("Bathtime!")
        self.pet.noise


class Pet:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 10

    def sleep(self):
        self.energy += 25
        print("Pet: I love walks! I feel so much energy!")

    def eat(self):
        self.energy += 5
        self.health += 10
        print("Pet: Yum, yum, yum, yum, yum, yum, yum, yum")

    def play(self):
        self.health += 5
        print("Pet: This is so fun! Wheeeeeeeeee!")

    def noise(self):
        print("ROOOOOOOOAAAAAAAARRRRRR!")


new_ninja = Ninja("Sam", "Jones", "bones", "food", "dog")
print(new_ninja)
