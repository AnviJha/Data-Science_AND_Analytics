#write a list comprehension to print a list which contains the multiplication table of a user entered number

# List comprehension is a short and powerful way to create lists in one line.
# [expression for item in iterable]

num=int(input("enter a number: "))
list=[1,2,3,4,5,6,7,8,9,10]

table=[i*num for i in list]

# another way 
tables=[i*num for i in range(1,11)]

print(table)
print(tables)