# write a class "Complex" to represent complex number along with overloaded operator " +" ans"*" which adds and multiplies them.

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

        #overload + operator  
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    # overload * operator
    def __mul__(self, other):
        real_part=(self.real*other.real)-(self.imag*other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return Complex(real_part, imag_part)

       # for clean output
    def __str__(self):
        return f"{self.real} + {self.imag}i"

# creating objects
c1 = Complex(2, 3)
c2 = Complex(4, 5)

# operations
print("Addition:", c1 + c2) #c1 + c2 → calls c1.__add__(c2)
print("Multiplication:", c1 * c2)#c1 * c2 → calls c1.__mul__(c2)