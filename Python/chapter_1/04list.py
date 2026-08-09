#  Print positive and negative elements of an List?
ls=[1,2,3,-1,-2,-3,0]
for i  , val in enumerate(ls):
    if val>0:
        print("positive number :", i, "-->", val)
    else:
        print("negative number :", i, "-->", val)
#  Mean of List elements?
print("---------------------------------------------------------")
mean=sum(ls)/len(ls)
print("mean of  the list :", mean)

# Find the greatest element and print its index too?
print("---------------------------------------------------------")
greatest=max(ls)
print("greatest element :",greatest)

# Find the second greatest element?
print("---------------------------------------------------------")
secondgreatest=sorted(ls)[-2]
print("second greatest element :",secondgreatest)
#  Check if List is sorted or not.
print("---------------------------------------------------------")
is_sorted=ls==sorted(ls)
print("is the list sorted :",is_sorted)
