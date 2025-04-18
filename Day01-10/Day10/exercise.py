## Leap Year Program
def is_leap_year(year):
    """Return True if the given year is a leap year, else False."""
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

year = int(input("Enter the year: "))
output = is_leap_year(year)
print(output)
