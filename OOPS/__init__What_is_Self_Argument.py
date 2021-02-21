#__init__ : what is self argument?

#-> It is the object that we will be refering to.

class PlayerCharacter:
    membership = True
    def __init__(self, name, age): #What is self?
        self.name = name #attribute
        self.age = age

    def shout(self):
        return self

player1 = PlayerCharacter('Alex','30')
print(player1)       # Returns class object
