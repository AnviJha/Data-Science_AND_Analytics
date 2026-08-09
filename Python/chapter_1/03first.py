# display a user entered name followed by good afternoon using input function
# name=input("enter the name : ")
# print("good afternoon !",name)

# #fill in the letter template :date and name 

# letter='''
#     Dear <|Name|>,
#     you are selected!
#     <|Date|>
#     '''
# print(letter.replace("<|Name|>",name).replace("<|Date|>","22-03-2026"))

#WAP to detect double space in string
space="i AM crazy over  you"
print("space index :",space.find("  "))

#Replace the double space from problem 3 with single space 
# method 1
ans=space.replace("  "," ")
print("replace space: ",ans)
# method 2 
result=" ".join(space.split())
print("after joining: " , result)

# strings are immutable,original string will remain same 
print("original string :",space)

# WAP too format the following letter using escape sequence character
Letter="Dear Anvi,\nyou can do it !"
print(Letter)