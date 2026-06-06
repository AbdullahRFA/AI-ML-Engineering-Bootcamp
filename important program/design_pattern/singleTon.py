'''
Singleton Design Pattern is a software design pattern that restricts the instantiation of a class to a single instance and provides a global point of access to that instance. This is useful when exactly one object is needed to coordinate actions across the system. The singleton pattern ensures that a class has only one instance and provides a global point of access to it.

In Python, you can implement the singleton pattern using various methods, such as using a class variable to store the instance, using a decorator, or using a metaclass. The example below demonstrates a simple implementation of the singleton pattern using a class variable to store the instance.


'''



# class Singleton:
#     _instance = None
    
#     def __new__(cls):
#         if cls._instance is None:
#             print("Instant Creating")
#             cls._instance = super().__new__(cls)
#             print("Instant Created")
#         return cls._instance
#     def getMessage(self):
#         print("This is singleton instance")
    
# obj1 = Singleton()
# obj2 = Singleton()

# obj1.getMessage()
# obj2.getMessage()

# if obj1==obj2:
#     print("Obj1 == obj2")
#     print("Obj1 id = ",id(obj1))
#     print("Obj2 id = ",id(obj2))
# else:
#     print("Obj1 != obj2")



class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Connecting to database...")
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Database Connected"
        return cls._instance

    def get_connection(self):
        return self.connection


db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.get_connection())
print(db2.get_connection())

print(db1 is db2)  # True
            