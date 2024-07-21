'''
Tip Calculator 
'''

print("Welcome to tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much % tip you want to give? 10, 12, or 15? ")
split_people = input("How many people to split the bill? ")

total_bill = int(bill) + (float(bill) * (float(tip) / 100)) # bill + %tip
bill_per_person = total_bill / int(split_people)

print(f"Each person should pay: ${bill_per_person: .2f}") # : .2f, two digit after decimal.
