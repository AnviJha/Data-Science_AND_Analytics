# file handling in python :creating ,reading ,writing ,updating file 


# opening a file :# f = open("file.txt", "mode")
# mode : 'r' ,'w','a','x'

# f=open("file.txt",'r')
# # read full file
# data=f.read()
# print(data)
# f.close()

# # read line by line ,in this method but there is space between lines printed
# f=open("file.txt",'r')
# for line in f:
#     print(line)
# f.close()    



# read +write open data
# ✅ Read + write both
# ❌ Error if file does NOT exist
# 📍 Pointer at beginning
# ⚠️ Writing overwrites from current position

f=open("file.txt",'r+')
f.write("hello world") #pointer starting mai hota hai toh delete nahi hota ,content starting mai add ho jata hai
print(f.read())
f.close()



