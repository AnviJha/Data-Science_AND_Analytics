# built a game rock paper and scissor 
import random
computer=random.choice([1,0,-1])

user={'r':0,'p':1,'s':-1}
revuser={0:'r',1:'p',-1:'s'}

choose=input("enter your choice : ")

your_choice=user[choose]

if(your_choice==computer):
    print("Its a draw")
else:
    if(your_choice==0 and computer==1):
        print(f'you win !')
    elif(your_choice==0 and computer==-1):
        print(f'you win !')    
    elif(your_choice==1 and computer==0):
        print(f'computer win !')        
    elif(your_choice==-1 and computer==0):
        print(f'computer win !')        
    elif(your_choice==1 and computer==-1):
        print(f'computer win !')  
    elif(your_choice==-1 and computer==1):
        print(f'you win !')   
    else:
        print("something went wrong")                  
