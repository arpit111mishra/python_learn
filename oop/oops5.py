#static methods--don't use self parameters.
class Student:
    college_name="Arpit's School"    
    def __init__(self,name,marks):
        self.name=name             
        self.marks=marks
    def display(self):  
        print(self.name,self.marks)
    @staticmethod                      #decorator
    def hello():
        print("helllo world")   #static method    
s1=Student("Arpit",100)
s1.display()
Student.hello()
s1.hello()



     