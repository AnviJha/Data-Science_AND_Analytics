# create a class (2d vector )and use it to create another class representing a 3D vector
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def   show(self):
        print(f'2D VECTOR ( X axis: {self.x} , Y axis:{self.y} )')  

class Vector3D(Vector2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)  #reuse 2d vectors 
        self.z=z
    def show(self):
        print(f'3D VECTOR ( X axis: {self.x} , Y axis:{self.y} ,Z axis: {self.z} )') 


# creating objects        
v2=Vector2D(2,3)
v3=Vector3D(4,5,6)
v2.show()
v3.show()    