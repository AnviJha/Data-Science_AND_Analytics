# /create a class employee and add salary and increment properties to it 
'''
class employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment
    @property #@property converts a method into an attribute (variable-like access).
    def salary_after_increment(self):
        return self.salary +(self.salary*self.increment/100)
    
e1=employee(5000000,10)
print(f'salary after increment : {e1.salary_after_increment}')

'''

#using getter and setter 
class Employee:
    def __init__(self,salary):
        self._salary=salary
        # private like

    @property
    def salary(self):
        return self._salary    
    
    @salary.setter
    def salary(self,value):
        if(value<0):
            print("invalid salary")
        else:
            self._salary=value

e=Employee(50000)                

print(e.salary) #getter
e.salary=-100 #setter validation