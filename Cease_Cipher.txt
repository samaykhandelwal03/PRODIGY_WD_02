def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Shift the character by the specified value
            char_code = ord(char)
            encrypted_char = chr((char_code - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            
            result += encrypted_char
        else:
            # If the character is not alphabetic, keep it unchanged
            result += char
    
    return result

def decrypt(text, shift):
    # Decryption is the same as encryption with a negative shift value
    return encrypt(text, -shift)

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted_message = encrypt(message, shift)
    decrypted_message = decrypt(encrypted_message, shift)
    
    print("\nEncrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
