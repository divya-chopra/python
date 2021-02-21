#dunder method
#-> Special methods
#-> Can be used as object.__str__() or str(object)
#-> Can modify dunder method definition for a class
#-> Custom modification of classes

class Toy:
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age
        self.my_dict = {
            "name": "Betty",
            "has_pets": False
        }

    def __str__(self):
        return self.colour

    def __len__(self):
        return 5

    def __del__(self):
        print("deleted")

    def __getitem__(self,i):
        return self.my_dict[i]

    def __call__(self):
        return("yess??")

action_figure = Toy("red", 0)
print(action_figure.__str__())
print(str(action_figure))
print(action_figure.__len__())
#del action_figure
print(action_figure['name'])
print(action_figure())
