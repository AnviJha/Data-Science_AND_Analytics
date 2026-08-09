# writing to file

# ✅ Creates file if not exists
# ⚠️ Deletes ALL old content (overwrite)
# 📍 Pointer at beginning

# f=open("file.txt","w")
# f.write("end!")
# f.close()       #this will erase old data


# ✅ Read + write
# ⚠️ Deletes old content
# ✅ Creates file if not exists

# 👉 Use when: Fresh file + also read

f=open("file.txt","w+")
f.write("duniya kharab hai") #cursor last mai aa gaya hai 
data=f.read()
print(data)
f.close()