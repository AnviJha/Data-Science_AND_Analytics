# a file contains a word donkey multiple times .you need to write a program which replace this word with ##### by updating the same file 
import os
# create file 
filename=(f'file_practice/Dumb_animals.txt')

with open(filename,'a',encoding="utf-8") as f:
    text=input("enter your thoughts: ")
    f.write(text)

with open(filename,'r') as f:
    content=f.read()
    contentnew=content.lower().replace("donkey","#####")   

with open(filename,'w',encoding="utf-8") as f:
    content=f.write(contentnew)
        