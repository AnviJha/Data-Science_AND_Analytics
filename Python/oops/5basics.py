#can you change the self_parameter inside a class to something else (say "Harry").
# Try changing self to "slf" or "harry " and see the effects.


# ans: yes you can change self to any name ,self is just a convention not a keyword 
class info:
    def __init__(harry,name):
        harry.name=name

    def display(harry):
        print("Name:",harry.name)

obj=info("anvi")
obj.display()