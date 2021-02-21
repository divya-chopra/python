#super()
#-> super() allows to refer super class 
#-> No need to pass self

class User:
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print("Signed In")

#Sub class inheriting User class
class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)             #  To pass constructor calue of parent or super class
        self.name = name
        self.power = power

    def attack(self):                   # Same method name but different function based on the object that calls it
        print(f'Attacking with power of {self.power}')

#Sub class inheriting User class
class Archer(User):
    def __init__(self, name, numOfArrows):
        self.name = name
        self.numOfArrows = numOfArrows

    def attack(self):                   # Same method name but different function based on the object that calls it
        print(f'Attacking with arrows: arrows left : {self.numOfArrows}')


#instantiate Wizard class
wizard1 = Wizard('Aby', 50, 'aby@gmail.com')
archer1 = Archer('Robin', 100)
print(wizard1.email)