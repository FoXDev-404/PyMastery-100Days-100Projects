def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):  # Loop through odd numbers cuz even nums are already non-prime
        if num % i == 0:
            return False

    return True


number_to_check = int(input("Enter the number you want to check: "))
result = is_prime(number_to_check)
print(result)
