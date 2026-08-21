# #list is muttable but tuple is immutable

# # WAP to store seven fruits in a list entered by the user

list=["Mango","Orange","Banana","guava","pineapple","apple","papaya"]
# print(type(list))

# # Wap to accept marks of 6 students and display them in a sorted manner

report=[]
for i in range(6):
    student,marks=input("Enter student name and marks : ").split()
    report.append((student,marks))
report.sort()    
print(report)    


# check that a tuple cannot be changed in python

# WAP to count the number of zeros in the following tuple 

# a=(7,0,8,0,0,9)
# c=a.count(0)
# print(a)
# print(c)
# # single element tuple
# t=(1,) #t=(1) not a tuple just an integer
# tup=1,2,3
# d,e,f=tup
# print(d,e,f)

# WAP to sum alist with 4 numbers
sum=[]
ans=0
for n in range(4):
    num=int(input("Enter number : "))
    sum.append(num)
    ans+=num
print(sum)    
print("sum of numbers : ",ans)