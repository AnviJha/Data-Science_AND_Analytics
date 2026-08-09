import math

# # WAP to print multiplication table of a given number usingn for loop 
# n=int(input("enter number : "))
# for i in range(1,11):
#     print(n," * ",i," = ",n*i)


# # WAP to greet all the person names stored in a list 'l' and which starts with s
# l=["Harry","Soham","Sachin","rahul"]
# for word in l:
#     if(word[0]=="S"):
#         print("hello ",word)


# # WAP to find the given number is prime or not
# n=int(input("Enter number : "))
# if(n<=1):
#     print("Not prime")
# else:    
#     for i in range(2,int(math.sqrt(n))+1):
#         if(n%i==0):
#             print("Not prime")
#             break
#     else:   #we used for else loop : else will apply when for is completely executed
#         print("Prime")    



# # sum of first n natural number 
# i=1
# sum=0
# n=int(input("enter number : "))
# while(i<n):
#     sum+=i
#     i+=1
# print(sum)    



# #WAP to calculate the factorial of  a given number using for loop
# n=int(input("enter number : "))
# fact=1
# for i in range(n,0,-1):   #default step is +1 therefore step need to be mentioned as -1
#     fact=fact*i
# print(fact)    


# WAP to print following star pattern
# for i in range(3):
#         print("*"*(2*i+1))
      

# # pattern 2
# for i in range(1,4):
#         print("*"*i)


# pattern 3
n = int(input("Enter number: "))

for i in range(1, n+1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n-2) + "*")
        


# # WAP to print multiplication table of n using for loops in reversed order
# n=int(input("Enter number : "))
# for i in range(10,0,-1):
#         print(n," * ",i," = ",n*i)


