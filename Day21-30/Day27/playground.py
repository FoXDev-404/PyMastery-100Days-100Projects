# ====== Unlimited Arguments ====== #
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(*range(1, 101)))  # Output: 5050

# ====== Kwargs (Keyword Arguments) ====== #
def calculate(n,**kwargs):
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")
    n += kwargs['add']
    n *= kwargs['multiply']
    print(f"Result: {n}")
calculate(2, add=3, multiply=5)
# Output: Result: 25

# ====== Defining a class that uses **kwargs in the constructor ====== #
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R", color="Red", seats=2)
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)