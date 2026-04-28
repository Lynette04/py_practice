class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        return "This is a " + self.brand + " and its model is a " +self.model +"."
    
    def car_info(self):
        message = self.display_info()
        print("Thank you for shopping with us! "+message)

car1 = Car("Toyota", "Sedan")
car2 = Car("Nissan", "SUV")

car1.car_info()
car2.car_info()