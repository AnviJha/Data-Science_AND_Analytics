# write a program to open three files 1.txt,2.txt,3.txt if any 
# these files are not present a message without exiting the program ,ust be printed prompting the same 

files=["Advance\\1.txt","Advance\\2.txt","Advance\\3.txt"]
for file in files:    
    try:
        with open(file,'r') as f:
            print(f'{file} opened successfully ! ')
        
    except FileNotFoundError:
        print(f"{file} not found. creating it now ...")
        with open(file,"w") as f:
            f.write("File created\n")

