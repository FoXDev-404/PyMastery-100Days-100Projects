# Caesar Cipher
# A classic encryption method where each letter in the message is shifted 
# by a fixed number of places in the alphabet. Named after Julius Caesar.

from art import logo
import os

print(logo)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # Adjust direction
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"\n🔐 Here is the {encode_or_decode}d result: {output_text}")

# Loop until user says 'no'
while True:
    direction = input("\n📌 Type 'encode' to encrypt or 'decode' to decrypt:\n> ").lower()

    if direction not in ["encode", "decode"]:
        print("❌ Invalid option. Please type 'encode' or 'decode'.")
        continue

    text = input("📝 Type your message:\n> ").lower()
    shift = int(input("🔁 Type the shift number:\n> "))
    shift = shift % len(alphabet)  # Normalize shift

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("\n🔄 Type 'yes' to go again. Type 'no' to exit:\n> ").lower()
    if restart != 'yes':
        print("\n👋 Goodbye, friend! Stay encrypted 😎")
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
