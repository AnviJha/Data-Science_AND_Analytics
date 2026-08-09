# dictionary store key value pair and ordered and immutable
d={                 
    "a":1,
    "b":2,
    "c":3
}

# get
print(d.get("a"))  #1
print(d.get("d"))   #None
# print(d["d"]) #this will give error 
print(d.get("d",0)) #0

# get all keys 
print(d.keys())
print(d.values())

#get key value pair
print(d.items()) 

# update
d.update({"b":5 ,"f":8})
print(d)

# pop
d.pop("c")
print(d)
d.popitem() #remove last element
print(d)
d.clear()
print(d)

print("---------------------------------------------------------")
#  Write a Python script to merge two Python dictionaries?
dict1={"a":10 , "b":20}
dict2={"c":30 , "d":40}
merged_dict = dict1 | dict2

print(merged_dict)

#  Write a Python program to sum all the values in a dictionary?
for i in 
#  Count the frequency of each element
#  Write a Python program to combine two dictionary by adding values for common keys.