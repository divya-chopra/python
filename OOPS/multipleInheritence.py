#Multiple Inherience
#-> Inheriting from 2 or more classes

class User:
    def sign_in(self):
        print("Signed In")

#Sub class inheriting User class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

#Sub class inheriting User class
class Archer(User):
    def __init__(self, name, numOfArrows):
        self.name = name
        self.numOfArrows = numOfArrows

    def check_arrows(self):
        print(f'Attacking with arrows: arrows left : {self.numOfArrows}')

    def run(self):
        print("Ran really fast")

class Hybrid(Wizard, Archer):
    def __init__(self, name, numOfArrows, power):
        Archer.__init__(self, name, numOfArrows)
        Wizard.__init__(self, name, power)

#instantiate Wizard class
wizard1 = Wizard('Aby', 50)
archer1 = Archer('Robin', 100)
hybrid1 = Hybrid('Heebo', 80, 99)

print(hybrid1.attack())
print(hybrid1.check_arrows())
print(hybrid1.sign_in())