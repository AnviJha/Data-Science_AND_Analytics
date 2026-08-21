# WAP to generate multiplication table from 2-20 and write it to the different files .place these files in a folder for a 13_year old.
import os
folder="Tables"
os.makedirs(folder,exist_ok=True)

num=int(input("Enter the number you want table of (2,20): "))
if num not in range(2,21):
    print("invalid input ! ")

# generate table 
def table(num):
    # we need to include the path in filename
    filename=f'{folder}/table_{num}.txt'
    with open(filename,"w") as f:
        for i in range(1,11):
            f.write(f'{num} * {i} = {num*i}\n')

    print(f"✅ File saved in {filename}")        

# function call
table(num)
