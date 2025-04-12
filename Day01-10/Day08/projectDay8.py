# Caesar Cipher - A simple encryption technique where each letter in
# the plaintext is shifted a certain number of places down the alphabet.
# Named after Julius Caesar.

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# diresction = input("Type 'encode' to encode, type 'decode' to decode:\n").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


# TODO-1: The encrypt() function
# def encrypt():
#     original_text = list(text)
#     shift_amount = shift
#     encrypted_text = []
#     for letter in original_text:
#         shifted_index = alphabet.index(letter) + shift_amount
#         shifted_index %= len(alphabet) # 0-25 index range
#         encrypted_char = alphabet[shifted_index]
#         encrypted_text.append(encrypted_char)
#     print(f"Encrypted message is: {''.join(encrypted_text)}")
# encrypt()
    
def encrypt(original_text, shift_amount):
    cipher_text = ''
    
    for letter in original_text:
        shifted_position = alphabet.index(letter)+shift_amount
        
        shifted_position%=len(alphabet) # 0-25 index
        cipher_text+= alphabet[shifted_position]
    print(f"Encodec message: {cipher_text}")
encrypt(original_text=text, shift_amount=shift)


# TODO-2: The decrypt() function
# def decrypt():
#     original_text = list(text)
#     shift_amount = shift
#     decrypted_text = []
#     for letter in original_text:
#         shifted_index = alphabet.index(letter) - shift_amount
#         shifted_index %= len(alphabet)  # ensures wrap-around
#         decrypted_char = alphabet[shifted_index]
#         decrypted_text.append(decrypted_char)
#     print(f"Decrypted message is: {''.join(decrypted_text)}")

# decrypt()


def decrypt(original_text, shift_amount):
    output_text = ''
    
    for letter in original_text:
        shifted_position = alphabet.index(letter)-shift_amount
        
        shifted_position%=len(alphabet) # 0-25 index
        output_text+= alphabet[shifted_position]
    print(f"Decrypted message is: {output_text}")
decrypt(original_text=text, shift_amount=shift)