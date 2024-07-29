# find word in file 
word = "mishra"
with open("file1.txt", "r") as f:
    data = f.read() 
print(data.index(word))
print(word in data)