#Methods
class Student:
    college_name="Arpit's School"    
    def __init__(self,name,marks):
        self.name=name             
        self.marks=marks
    def display(self):    #with methods always use self
        print(self.name,self.marks)
s1=Student("Arpit",100)
s1.display()
s2=Student("Aadi",56)
s2.display()


     