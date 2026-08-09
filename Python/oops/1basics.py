# create a class "programmer" for storing information of new programmers working at microsoft 
class programmer:
    def __init__(self,name,employee_id,language,experience):
        self.name=name
        self.employee_id=employee_id
        self.company="Microsoft"
        self.language=language
        self.experience=experience
    
    def display_info(self):
        print("PROGRAMMERS DETAIL :")
        print(f'NAME:{self.name}')
        print(f'ID : {self.employee_id}')
        print(f'COMPANY :{self.company}')
        print(f'LANGUAGE : {self.language}')
        print(f'EXPERIENCE : {self.experience}')
        

# creating object
p1=programmer("Anvi",101,'python',5)
p2=programmer("himanshu",102,'genai',5)

# using method
p1.display_info()
print()
p2.display_info()

    
