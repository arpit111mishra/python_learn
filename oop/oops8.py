#private
class Student:
    def __init__(self,name):
        self.__name=name
    def __hello(self):           #private methods
        print("hey")      
s1=Student("Arpit")
#print(s1.__name)        #private can't be accessiable    error


