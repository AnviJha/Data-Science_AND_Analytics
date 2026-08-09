#write a class calculator capable of finding square ,cube and square root of a number 
# Add a static method in 2 to greet the user with hello 

import math

class Calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        return self.num*self.num

    def cube(self):
        return self.num*self.num*self.num

    def square_root(self) :
        return math.sqrt(self.num)
       
    @staticmethod
    def greet():
        print("Hello ji")


c=Calculator(16)
c.greet()
print("Square:",c.square())
print("cube:",c.cube())
print("square root:",c.square_root())