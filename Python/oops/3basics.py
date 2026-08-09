# create a class with a class attribute a;create an object from it and set 'a' directly using object.a=0.does this change the class attribute 

# class vs instance attribute 

class attri:
    a=10  #class attribute unchanged

object=attri()

object.a=0  #new instance attribute created ,object has now its own copy of a 

print(object.a) 
print(attri.a)   

# Python does NOT change the class attribute
# Instead, it creates a new instance attribute a for obj

# Assigning via object creates/updates instance attribute, not class attribute