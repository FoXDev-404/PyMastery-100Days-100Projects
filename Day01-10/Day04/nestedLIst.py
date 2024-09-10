# Nested list in Python and IndexError

# Nested list
# nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nestedList)
#
# # or
# fruits_list = ['Apple', 'Banana', 'Orange' 'Pineapple', 'Mango', 'Grapes']
# vegetables_list = ['Tomato', 'Potato', 'Carrot', 'Onion']
#
# nestedList = [fruits_list, vegetables_list]
# print(nestedList)

#* IndexError
my_list = ["Alice in Wonderland", "The Lion King", "The Jungle Book", "The Godfather",
            "The Dark Knight", "The Shawshank Redemption, Naruto", "One Piece", "Dragon Ball Z",
            "Attack on Titan", "Death Note", "Tokyo Ghoul", "My Hero Academia", "Demon Slayer",
            "Black Clover", "One Punch Man", "Bhool Bhulaiyaa", "Dil Chahta Hai", "Kabhi Khushi Kabhie Gham",
            "Kabir Singh", "Uri: The Surgical Strike", "Baahubali: The Beginning", "Baahubali 2: The Conclusion",
            "Dangal", "PK", "3 Idiots", "Lagaan", "Swades", "Chak De! India", "Rang De Basanti", 
            "Dilwale Dulhania Le Jayenge", "Kuch Kuch Hota Hai", "Mohabbatein", "Kabhi Alvida Naa Kehna",]

length = len(my_list) # 33

# IndexError
# print(my_list[length]) # IndexError: list index out of range
print(my_list[length-1]) # Kabhi Alvida Naa Kehna, at index 32 last element
