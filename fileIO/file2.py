#writing to a file
f=open("/Volumes/Code/python/fileIO/demo.txt","w")
f.write("overrites then write")
f.close()
f=open("/Volumes/Code/python/fileIO/demo.txt","a")
f.write("don't override just appen at ends")
f.close()
f=open("/Volumes/Code/python/fileIO/demo.txt","r+")  #trunncate and then write on start read and write
f.write("zbc")
f.close()
f=open("/Volumes/Code/python/fileIO/demo.txt","a+")  
f.write("zbcadeafc")
f.close()