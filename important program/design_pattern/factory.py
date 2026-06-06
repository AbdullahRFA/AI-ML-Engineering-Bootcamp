'''
Factory Design Pattern is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. It promotes loose coupling by eliminating the need to bind application-specific classes into the code. The factory method creates objects without exposing the instantiation logic to the client and refers to the newly created object through a common interface. The factory pattern is often used when the exact type of object to be created is not known until runtime, or when the creation process is complex and needs to be centralized in one place. The example below demonstrates a simple implementation of the factory design pattern in Python, where a factory class is responsible for creating instances of different vehicle types based on the input provided by the client.   



'''


class bike:
    def driver(self):
        return "Driving a bike"
    
class car:
    def driver(self):
        return "Driving a car"
    
class vehicleFactory:
    @staticmethod
    def getVehicle(vehicleType):
        if vehicleType == "bike":
            return bike()
        elif vehicleType == "car":
            return car()
        else:
            return "Unknown vehicle type"
        
        
        
vehicle1 = vehicleFactory.getVehicle("bike")
vehicle2 = vehicleFactory.getVehicle("car")
vehicle3 = vehicleFactory.getVehicle("bus")  # Unknown vehicle type

print(vehicle1.driver())
print(vehicle2.driver())
print(vehicle3)
