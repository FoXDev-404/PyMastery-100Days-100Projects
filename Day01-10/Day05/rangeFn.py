# Range function with loop

for number in range(1,101):
    print(number)
    
# Sum of 1 to 100
sum = 0
for number in range(1,101):
    sum += number
print(sum)

for numbers in range(1,101):
    if numbers%3 ==0 and numbers%5==0:
        print("FizzBuzz")
    elif numbers%3==0:
        print("Fizz")
    elif numbers%5==0:
        print("Buzz")
    else:
        print(numbers)