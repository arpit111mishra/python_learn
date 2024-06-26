#constructor
class Student:
    def __init__(self):   #default
        pass
    def __init__(self,name):    #parameterized constructor
        print(self)    #same memory address as current object
        self.name=name
        print(name)
s1=Student("arpit")        

