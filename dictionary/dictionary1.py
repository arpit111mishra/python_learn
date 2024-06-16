dic={
    "name":"arpit",
     "class":"Mca",     #key:value,
    "college" :"LPU",
    "age":22,
    "subjects":["python","database","linux","os"],  #in dictionary we can add list and tuple  
}
print(dic["name"],dic["college"])
print(dic)
null_dict={}   #null dict
#nested dictionary
dict1={
    "name":"arpit",
    "score":{
        "python":99,
        "dbms":99,
        "cpp":100
    },
    "class":"MCA"
}
print(dict1)
print(dict1["score"])
print(dict1["score"]["dbms"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.get("name"))
dict1.update(dic)
print(dict1)
print(len(dict1))