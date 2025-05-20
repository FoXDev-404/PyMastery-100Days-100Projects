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