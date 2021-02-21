#Pillars of OOP -> Inheritence
#-> Allows new object to take properties of previous classes
#-> isinstance(instance, class) -> built in function in python to check
#-> Everything in python is an object and object class is inherited by all the components

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

    def attack(self):
        print(f'Attacking with arrows: arrows left : {self.numOfArrows}')

#instantiate Wizard class
wizard1 = Wizard('Aby', 50)
archer1 = Archer('Robin', 100)

wizard1.attack()
archer1.attack()


# Checking isinstance() built in function

print(isinstance(wizard1, Wizard))      # True
print(isinstance(wizard1, User))        # True as User class is inherited
print(isinstance(wizard1, object))      # True as everything in python is inherited from object class