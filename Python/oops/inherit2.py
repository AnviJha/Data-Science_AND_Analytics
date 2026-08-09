# create a class pets from a class animals and further create a class dog from pets add a method bark to class dog

class Animals:
    def __init__(self):
        print(f'stay away from wild animal')


class Pets(Animals):
    def __init__(self,type):
        super().__init__()
        self.type=type
        print(f' The type of pet i am having is  {self.type}')

class Dog(Pets):
   
    def bark(self):
        print(f'The {self.type} barks "bow bow !"')


d1=Dog("Doggy")
d1.bark()
