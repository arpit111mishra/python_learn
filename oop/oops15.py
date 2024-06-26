#polymorphism : operator overloading
#implicit 
# print(1+2)
# print("arpit" + "mishra")    one operator different work    .implicit provided by programming lang
# print([1,2,3]+[5,6,7])
#explicit   ---creted by us
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i",self.img,"j")
    # now we have to write a method to calculate the addition of complex number .which we can do with dunder function(__ vale function)    
    # def add(self,num2):          dunder function nhi hai   eske liye num1.add(num2)   yese call krna pdega
    #     newReal=self.real+num2.real
    #     newImg=self.img+num2.img
    #     return Complex(newReal,newImg)
    def __add__(self,num2):         #dunder function now we can call through num1 +num2 yha def __add__(num1,num2) bhi kr sakte self ki jgh
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    def __sub__(self,num2):          
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)

num1=Complex(1,3)
num1.showNumber()
num2=Complex(6,7)  
num2.showNumber()          
# num3=num1.add(num2)  pr esko na likh kr agr simple num1 +num2 likhna cahte to dunder function ka use usko sirf __ lgane se bn jayega   
num3=num1+num2
num3.showNumber()
num4=num1-num2
num4.showNumber()