# Pillers of OOP -> Abstraction
#->Hiding/abstracting information and providing access to information that is necessary to users/ machine.

# Public and Private variables
#-> In python there is no true private keyword for variable
#-> Need to add _in front of variable name as part of naming convention
#-> _variablename should not be modified


class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self._name = name #private variable
        self._age = age

    def shout(self):
        print(f'my name is {self.name} and my age is {self.age}')

player1 = PlayerCharacter('Ted', 30)
player1.shout()         #Abstraction in action

print((1,2,3,1).count(1))     #Tuple class in action
print(len((1,2,3,4,5)))       #Built in function


player1.name='Error'         # Able to change object variable. Bad practice to overwrite private variable
player1.shout()             