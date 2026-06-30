'''
Builder Pattern: The Builder pattern is a design pattern that allows for the step-by-step construction of complex objects. It separates the construction of an object from its representation, allowing the same construction process to create different representations. The Builder pattern is particularly useful when an object needs to be created with many optional parameters or when the construction process is complex and needs to be controlled. The example below demonstrates a simple implementation of the Builder pattern in Python, where a ComputerBuilder class is used to construct a Computer object with various components such as CPU, RAM, and storage. The builder provides methods to set each component and a build method to return the final Computer object. This approach allows for a more readable and maintainable way to create complex objects without having to deal with a large constructor or multiple constructors for different configurations. 

'''

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}, storage={self.storage})"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer
    

builder = ComputerBuilder()
computer = builder.set_cpu("Intel i7").set_ram("16GB").set_storage("512GB SSD").build()
print(computer) 