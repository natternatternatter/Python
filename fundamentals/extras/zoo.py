class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))

    def add_tiger(self, name):
        self.animals.append(Tiger(name))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


class Cat:
    def __init__(self, name):
        self.name = name

    def stalk

    def printmessage(self):
    print(self.message)


class Tiger(Cat):
    def __init__(self, name):
        super().__init__(name)


class Lion(Cat):
    def __init__(self, name):
        super().__init__(name)


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info
