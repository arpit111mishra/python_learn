# mutlilevel  inheritnce
class Car: 
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")
class Bmw(Car):
    def __init__(self,name):
        self.__name=name
    def print(self):
        print(f"car is {(self.__name)}")    
class Rr(Bmw):
    def __init__(self,number):
        self.number=number
        print(self.number)

car1=Rr("11234")
car1.start()
car1.stop()        
