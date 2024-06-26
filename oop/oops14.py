#property decorator
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math   #teen subject ke marks aa rhe and we are calculatng percentage
        self.percentage=str((self.phy+self.chem+self.math)/3)+" %"
        #def calcPersentage(self):               by method (way 2)
             # self.percentage=str((self.phy+self.chem+self.math)/3)+" %"
        @property
        def percentage(self):            #way 1 best way by property decorator
            return str((self.phy+self.chem+self.math)/3)+" %"
stu1=Student(98,97,99)
print(stu1.percentage)
#ab pata chala student ke phy ke marks glt lg gye hai
# and teachers ne marks bdl diye eg
stu1.phy=86
print(stu1.phy) #marks update ho gye physics ke 98 se 86 par agr hum ab bhi percentage print 
#karaye to vo purane vale marks se hi aayeenge update hokr nhi.
# esliye jab v kisi variable ki value fix na ho kisi calculation pr depend kre to 
# to hum  property decorator se (way 1 best way)ya (second way)method bna kr kaam kr sakte 
print(stu1.percentage)#ab update hota jayega apne aap har baar updatedd value ke sath calculate hokr print hoga
