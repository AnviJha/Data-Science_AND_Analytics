# # function to find greates of 3 number 
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c


# a,b,c=map(int,input("Enter numbers :").split())
# ans=greatest(a,b,c)
# print(ans)  


# # celcius to farenfeit
# def tempchange(c):
#     f=(9/5)*c+32
#     return f

# c=int(input("celcius degree "))
# print(tempchange(c))


# # prevent to print a new line at the end 
# print("dont end up in a new line",end=" ",)
# print("TO be continued...")


# # recursive function to print sum of first n natural number 
# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)

# num=int(input("Enter number : "))
# ans=sum(num)
# print(ans)

# # convert inches to cms 
# def ctm(inches):
#     cm=inches*2.54
#     return cm

# inch=int(input("enter number : "))
# print(ctm(inch))



# # WAP to remove word from a list ad strip it at the same 
# l = ["  apple  ", " banana", "mango ", "apple"]

# word = "apple"

# result = []

# for item in l:
#     clean = item.strip()   # remove spaces
#     if clean != word:      # remove word
#         result.append(clean)

#  print(result) 

# # WAp function to print multiplicatin of a number 
# def multiplication(n):
#      for i in range(1, 11):
#         print(n, "x", i, "=", n*i)


# num=int(input("enter number : "))
# multiplication(num)