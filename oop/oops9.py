#inheritence... //single inheritence 
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
car1=Bmw("s1 class")
car1.start()
car1.print()
car1.stop()        

                 