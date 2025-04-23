# The Print is friend, Squash bugs with a print() Statement

word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # Used an "==" comprision opeator not assignment operator
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)