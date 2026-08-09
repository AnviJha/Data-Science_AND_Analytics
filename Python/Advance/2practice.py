# write a program to print third fifth and seventh element from a list using enumerate function
watches = ["Rolex", "Omega", "Casio", "Fossil", "Titan", "Seiko", "Apple"]

# The enumerate() function is used to loop over something and keep track of the index (position) at the same time.
# iterable → list, tuple, string, etc.

for i,list in enumerate(watches,start=1):
    if(i==3 or i==5 or i==7):
        print(i,list)