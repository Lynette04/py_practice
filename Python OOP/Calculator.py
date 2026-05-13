#Create a simple scientific calculator 
import math

class Calculator:
    def addition(self,a,b):
        return a + b
    
    def multiplication(self,a,b):
        return a * b   
    
    def subtraction(self,a,b):
        return a - b
    
    def division(self,a,b):
        if b==0:
            print("Error!")
        else:
            return a / b
        
    def root(self,a):
        return math.sqrt(a)
        
    def sine(self,a):
        a=math.radians(a)
        return math.sin(a)
    
    def cosine(self,a):
        a= math.radians(a)
        full_cos = math.cos(a)
        return round(full_cos,10)
    
    def tan(self,a):
        a = math.radians (a)
        full_tan = math.tan(a)
        return  round(full_tan,10)     
        
calc = Calculator()
print(calc.addition(5,3) ) 
print(calc.multiplication(5,3))
print(calc.subtraction(5,3))
print(calc.division(5,3))  
print(calc.root(9))   
print(calc.sine(90))
print(calc.cosine(90))
print(calc.tan(45))