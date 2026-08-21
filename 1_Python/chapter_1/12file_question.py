# WAP tp read text from a gicen file and find out whether it contains the world twinkle 

# for small files only
with open("12poem.txt",'r') as f:
    data=f.read()
    if "Twinkle" in data:
        print("word found")
    else:
        print("word not found")



# for large files :
word = "star"

with open("12poem.txt", "r") as f:
    for line in f:
        if word in line:
            print("✅ Found:", line)