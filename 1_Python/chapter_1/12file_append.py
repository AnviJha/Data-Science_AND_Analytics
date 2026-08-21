# append : add data without deleting the old content 
# ✅ Creates file if not exists
# ➕ Adds data at the end
# ❌ Cannot read

# # 👉 Use when: You want to add data without deleting old
# f=open("file.txt",'a')
# f.write("i anm the new content")

# # after writing the cursor moves to end so we need to move it in front 
# f.seek(0)
# data=f.read()
# print(data)
# f.close()

# append+read
# ✅ Read + append
# 📍 Pointer at end
# ⚠️ Must use seek(0) to read

# 👉 Use when: Add + read existing content
f=open("file.txt",'a+')
f.write("love  ")
f.seek(0)
data=f.read()
print(data)
f.close()

