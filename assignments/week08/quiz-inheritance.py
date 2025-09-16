""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:

    def __init__(self, brand, model ,year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Vehicle: {self.year} {self.brand} {self.model}"
    
class Car(Vehicle):
    
    def __init__(self, brand, model, year, number_of_door):
        super().__init__(brand, model, year)
        self.number_of_door = number_of_door

    def get_info(self):
        return F"Car: {self.year} {self.brand} {self.model}, Door: {self.number_of_door}"
    
    
myCar = Car("Toyota","Gr86",2025,2)
print(myCar.get_info())