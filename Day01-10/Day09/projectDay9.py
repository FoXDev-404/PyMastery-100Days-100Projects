# Secret auction program project
import os

bid_dict = {}


while True:
    add_more = input(f"Any one else want to bid 'yes' or 'no': ").lower()
        
    if add_more == "yes":
        user = input("Enter Your name: ")
        bid_price = int(input("Enter the bid amount: $"))
        bid_dict[user] = bid_price
        # print(bid_dict)
    elif add_more == "no":
        break
    os.system('cls')


os.system('cls')    
max_bid = max(bid_dict,key=bid_dict.get)
print(f"Largest bid is ${bid_dict[max_bid]} by '{max_bid}'")