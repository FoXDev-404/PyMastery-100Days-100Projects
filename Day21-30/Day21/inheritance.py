# Class Inheritance
# Inheritance is a way to form new classes using classes that have already been defined.

class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Exhaling and inhaling")
    
class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def swim(self):
        print("Swimming in the water")
        
    def breathe(self):
        super().breathe()  # Call the method from the parent class
        print("Breathing underwater")
        
nemo = Fish()
nemo.breathe()  # Inherited from Animal class
nemo.swim()     # Defined in Fish class
print(nemo.num_eyes)  # Inherited from Animal class
        