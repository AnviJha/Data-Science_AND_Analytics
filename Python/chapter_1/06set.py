# set :ounordered collection of unique elements 
# /python uses hash table internally for set
# empty set
s=() #s={} is not empty set but empty dictionary
s1={9,7,8,6}
print(s1)
s2=set([1,2,3,4,1,2,3,4,1,2,3,4])
s1.add(5)
print(s1)
s1.update([1,2,3])
print(s1)
s1.remove(5) #error if not found
print(s1)
s1.discard(3) #no error when not found
print(s1)
s1.pop() #remove random element 
print(s1)

# union comnine set
print(s1.union(s2))
# intersection
print(s1.intersection(s2))
# difference()
print(s1.difference(s2))
#is subset()
print(s2.issubset(s1))