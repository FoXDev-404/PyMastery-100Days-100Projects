import pandas

def generate_phonetic():
    try:
        # Load data and create dictionary
        data = pandas.read_csv("nato_phonetic_alphabet.csv")
        phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
        
        while True:
            try:
                # Get user input
                user_input = input("Enter a word: ").upper()
                
                # Validate input contains only letters
                if not all(char.isalpha() or char.isspace() for char in user_input):
                    raise ValueError("Please enter only alphabetic characters.")
                
                # Generate phonetic list with error handling for each letter
                phonetic_list = [phonetic_dict[letter] for letter in user_input if letter.isalpha()]
                
                # Display result
                print(phonetic_list)
                break
                
            except KeyError as e:
                print(f"Error: Character '{e.args[0]}' is not in the NATO phonetic alphabet.")
            except ValueError as e:
                print(f"Invalid input: {e}")
                
    except FileNotFoundError:
        print("Error: NATO alphabet file not found. Please check that 'nato_phonetic_alphabet.csv' exists.")
    except pandas.errors.EmptyDataError:
        print("Error: The NATO alphabet file is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    generate_phonetic()
