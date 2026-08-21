# WAP to create a dictionary of hindi words with value as their english translation
# dict={
#     "namaste":"Hello",
#     "pani": "water",
#     "kitaab": "book",
#     "dost": "friend",
#     "khana": "food"
# }
# # user input
# word=input("enter word hindi : ")
# print(dict.get(word,"word not found"))


# WAP to input 8 numbers from the user and dislay all unique elements
# set=set()
# for i in range(8):
#     num=int(input("enter number :"))
#     set.add(num)
# print(set)    



# can we have a set with 18(int) and '18'(str)as a value in it
# no   ,Set cannot store key-value pairs
# s = {
#     (1, "a"), (2, "b"), (3, "c"), (4, "d"),
#     (5, "e"), (6, "f"), (7, "g"), (8, "h"),
#     (9, "i"), (10, "j"), (11, "k"), (12, "l"),
#     (13, "m"), (14, "n"), (15, "o"), (16, "p"),
#     (17, "q"), (18, "r")
# }

# print(s)


# # what will be the length of the following set
# s=set()
# s.add(20)
# s.add(20.0) #20 == 20.0   # True
# s.add('20')
# print(len(s))

# #create empty dict .allow 4 friends to enter their fav language as value and use key as their names ,assume that names are uniqque 
d={}
for i in range(4):
    name=input("Enter key : ")
    fav_lang=input("Enter value : ")
    d[name]=fav_lang
print(d)    


#if the names of 2 friends are same what will happen to the program in problem 6
   #the key value will get update and older value get discard 

#Can you change the value inside the list  which is contained in set S
     #no you can not put list inside set .Set elements must be hashable (immutable) . List is mutable (changeable) ❌



