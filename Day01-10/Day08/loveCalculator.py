def calculate_love_score(name1, name2):
    # Combine names and convert to lowercase
    combined_names = (name1 + name2).lower()

    # Letters to check
    true_letters = ["t", "r", "u", "e"]
    love_letters = ["l", "o", "v", "e"]

    # TRUE letter counts
    print("TRUE letter counts:")
    true_score = 0
    for letter in true_letters:
        count = combined_names.count(letter)
        print(f"{letter.upper()} occurs {count} time(s)")
        true_score += count

    # LOVE letter counts
    print("\nLOVE letter counts:")
    love_score = 0
    for letter in love_letters:
        count = combined_names.count(letter)
        print(f"{letter.upper()} occurs {count} time(s)")
        love_score += count

    # Final love score
    final_score = int(f"{true_score}{love_score}")
    print(f"\n❤️ Love Score = {final_score}")

calculate_love_score("Kanye West", "Kim Kardashian")

'''
# ***Only Prints the Score***

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    true_letters = ["t", "r", "u", "e"]
    love_letters = ["l", "o", "v", "e"]

    true_score = sum(combined_names.count(letter) for letter in true_letters)
    love_score = sum(combined_names.count(letter) for letter in love_letters)

    final_score = int(f"{true_score}{love_score}")
    print(final_score)

# Example usage
calculate_love_score("Nikhil Pratap Singh", "Lovely")
'''