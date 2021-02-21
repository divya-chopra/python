# @classmethod

#-> can use without even instantiating class
#-> Call it using classname.method_name(method arguments)
#-> 95% not useful
#-> Can be used to instantiate an object of class

 #@staticmethod

#-> Same as classmethod except no access to cls or class
#-> So we cannot instantiate class using static method
#-> Can perform any other function
#-> Use this when we don't need to use class attributes

class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name #attribute
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_age(cls, num1, num2):
        return cls('Teddy', num1 + num2) #Instantiating class

    @staticmethod
    def adding_score(stage1, stage2):    # no access to cls
        return(stage1 + stage2)

player1 = PlayerCharacter.adding_age(10,19) #class method called without instantiating class
print(player1.age)

player1_score = PlayerCharacter.adding_score(2,5) # Can be used without class is instanctiated
print(player1_score)