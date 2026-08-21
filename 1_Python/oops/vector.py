# vector of n dimension ,overlaod + and * calculate sum and dot product of them ,use__str__ for clean printing 
class Vector:
    def __init__(self,dim,*d):
        self.dim=dim
        self.data=list(d)

        if len(self.data) != dim:
            raise ValueError("Dimension and data size mismatch")
        

    def __add__(self, other):
        if self.dim != other.dim:
            raise ValueError("Vectors must have same dimension")

        result = [self.data[i] + other.data[i] for i in range(self.dim)]
        return Vector(self.dim, *result)
    
    def __mul__(self, other):
        if self.dim != other.dim:
            raise ValueError("Vectors must have same dimension")

        return sum(self.data[i] * other.data[i] for i in range(self.dim))

    
    def __str__(self):
        symbols = ['i', 'j', 'k', 'l', 'm']  # supports more dimensions
        terms = []

        for i in range(self.dim):
            terms.append(f"{self.data[i]}{symbols[i]}")

        return " + ".join(terms)



# creating vectors
v1 = Vector(3, 1, 2, 3)
v2 = Vector(3, 4, 5, 6)

# operations
print("v1:", v1)
print("v2:", v2)

print("Addition:", v1 + v2)
print("Dot Product:", v1 * v2)