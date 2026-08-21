# # WAP to find the greatest of four number entered by the user
# a=int(input("Enter number : ")) 
# b=int(input("Enter number : ")) 
# c=int(input("Enter number : ")) 
# d=int(input("Enter number : ")) 

# if(a>b and a>c and a>d):
#     print(a," is greatest")
# elif(b>a and b>c and b>d):
#     print(b," is greatest")
# elif(c>a and c>b and c>d):
#     print(c," is greatest")    
# else:
#     print(d,"is greatest")

# print("end of program")    



# # WAP to find out whether a student has passed or failed if it requires a total 40% and atleast 33% in each subject to pass.Assume 3 subjects and total marks as an input from the user
# sub1=int(input("marks of subject 1 : ")) #each subject paper is of 100 marks 
# sub2=int(input("marks of subject 2 : "))
# sub3=int(input("marks of subject 3 : "))

# p=((sub1+sub2+sub3)/300)*100 #percentage

# if(p>40 and sub1>33 and sub2>33 and sub3>33):
#     print("student has passed")
# else:
#     print("Student has failed")
        


# # spam  words :"Make a lot of money","Buy now",subscribe this","click this".WAP to detect these spam 
# text=input("enter mail ")
# if text.find("Make a lot of money")!=-1 or text.find("Buy now")!=-1 or text.find("subscribe this")!=-1 or text.find("click this")!=-1:
#     print("spam")
# else:
#     print("Not spam")  



# # WAP to find whether a given username contains less than 10 character or not
# username=input("enter your name please : ")
# length=len(username)
# if(length>10):
#     print("greater than 10 character")
# else:
#     print("less than 10 character")


# wap to find out whether a given post is talking about anvi or not
post=input("enter text : ")

if("anvi".lower() in post.lower()):
    print("Anvi there")
else:
    print("not there")    