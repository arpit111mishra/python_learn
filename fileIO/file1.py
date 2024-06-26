#reading a file.
f=open("/Volumes/Code/python/fileIO/demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()
#if want to read set of particular character to read then.....
f=open("/Volumes/Code/python/fileIO/demo.txt","r")
data1=f.read(5)    #read 5 characters from file
print(data1)
f.close()
# for reading line by line.....
f=open("/Volumes/Code/python/fileIO/demo.txt","r")
data2=f.readline()
print(data2)
data3=f.readline()
print(data3)
f.close()
