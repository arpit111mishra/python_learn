#attributes --class and instance
class Student:
    college_name="Arpit's School"    #class attribute
    def __init__(self,name,marks):
        self.name=name             #instance attribute
        self.marks=marks
s1=Student("AAddii",97)
print(s1.name,s1.marks)
s2=Student("Arpit",99)
print(s2.name,s2.marks)
print(Student.college_name)       #printing class attribute
     