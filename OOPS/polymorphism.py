#Pillars of OOP -> Polymorphism
#-> Poly -> Many, Morphism -> Form : Many forms
#-> Object methods can share same method names but methods can act differently based on the object that calls it.


class User:
    def sign_in(self):
        print("Signed In")

    def attack(self):
        print("Don't do anything")

#Sub class inheriting User class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):                   # Same method name but different function based on the object that calls it
        User.attack(self)               # If we need to run attack method of User class also
        print(f'Attacking with power of {self.power}')

#Sub class inheriting User class
class Archer(User):
    def __init__(self, name, numOfArrows):
        self.name = name
        self.numOfArrows = numOfArrows

    def attack(self):                   # Same method name but different function based on the object that calls it
        print(f'Attacking with arrows: arrows left : {self.numOfArrows}')


#instantiate Wizard class
wizard1 = Wizard('Aby', 50)
archer1 = Archer('Robin', 100)

for char in [wizard1, archer1]:        #calling same method but 2 different output
    char.attack()