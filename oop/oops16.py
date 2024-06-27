#multilevel inheritence
class A:
    def __init__(self,name):
        self.name=name
class B(A):
    def __init__(self,name,clas):
        super().__init__(name)
        self.clas=clas
class C(B):
    def __init__(self,name,clas):
        super().__init__(name,clas)
c=C("Arpit","MCA") 
print(c.name)
print(c.clas)