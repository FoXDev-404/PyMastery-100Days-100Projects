scores = [150,149,185,124,199,169,148,123,189,169]

print(max(scores)) # Using the max() function

# Using a loop to find the maximum score
max_score = 0
for score in scores:
    if  max_score < score:
        max_score = score
print(max_score)

## Trying something new

cars = ["Toyota", "Honda", "BMW", "Mercedes", "Audi", "Ford", "Chevrolet", "Jeep", "Nissan", "Hyundai"]
f_car = "BMW"
for car in cars:
    if car in f_car:
        print(car)