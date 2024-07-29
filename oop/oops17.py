#multiple inhertitence
class emp:
    def __init__(self,name):
        self.name=name
class Sing:
    def __init__(self,sing):
        self.sing=sing
class child(emp,Sing):
    def __init__(self,t,n,s):
        emp.__init__(self,n)
        Sing.__init__(self,s)
        self.t=t
C=child("classic","arpit","dil ki tapis")
print(C.t)
print(C.name)
print(C.sing) 