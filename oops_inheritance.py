
# first i created Base class (Parent class)
class Vehicle:
    def __init__(self, brand, model):
        # This attributes shared by all vehicles
        self.brand = brand
        self.model = model

    def start_engine(self):
        # parent class  method to start the engine
        print(f"{self.brand} {self.model}'s engine started.")

    def stop_engine(self):
        #  parent class method to stop the engine
        print(f"{self.brand} {self.model}'s engine stopped.")

# Car inherits from Vehicle (this is child class 1)
class Car(Vehicle):
    def __init__(self, brand, model, airbags):
        # now calling  the constructor of the base class
        super().__init__(brand, model)
        # Specific attribute for Car
        self.airbags = airbags

    def play_music(self):
        # Specific method for Car
        print(f"Playing music in {self.brand} {self.model}.")

    def car_info(self):
        # Showing car details
        print(f"Car: {self.brand} {self.model}, Airbags: {self.airbags}")

# Bike inherits from Vehicle (child class 2)
class Bike(Vehicle):
    def __init__(self, brand, model, has_gear):
        # Call the constructor of the base class
        super().__init__(brand, model)
        # Specific attribute for Bike
        self.has_gear = has_gear

    def do_wheelie(self):
        # Specific method for Bike
        print(f"{self.brand} {self.model} is doing a wheelie!")

    def bike_info(self):
        # Show bike details
        print(f"Bike: {self.brand} {self.model}, Gear: {'Yes' if self.has_gear else 'No'}")

# Creating a Car objects of all classes
my_car = Car("Toyota", "Fortuner", airbags=6)
my_car.start_engine()       # Inherited from Vehicle
my_car.play_music()         # Specific to Car
my_car.car_info()
my_car.stop_engine()        # Inherited from Vehicle

print("-----------------------")

# Creating a Bike object
my_bike = Bike("Yamaha", "R15", has_gear=True)
my_bike.start_engine()      # Inherited from Vehicle
my_bike.do_wheelie()        # Specific to Bike
my_bike.bike_info()
my_bike.stop_engine()       # Inherited from Vehicle
