# for change in class attribute
class Person:
    name="anonymous"
    #def changeName(self,name):
      #  self.name=name  ye class attribute ko chnage nhi kr payega.alg hi bna dega name attribute
      #  Person.name=name  # method 1 to change class attribute
      #  self.__class__.name=name   method 2 to change class attribute    ye dono
      # method se to change ho sakte class attribute par agr hum cahnte hai ki ye functoin 
      # se change ho to hum class methods ka use krte hai @classmethod  decorator ki hekl se
    @classmethod
    def changeName(cls,name): #cls =class self ki jgh
          cls.name=name
p1=Person()
p1.changeName("arpit")
print(p1.name)