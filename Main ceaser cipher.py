def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts the given text using the Caesar cipher.

    Args:
        text (str): The input text (either plaintext or ciphertext).
        shift (int): The shift value (positive for encryption, negative for decryption).
        mode (str): 'encrypt' or 'decrypt'.

    Returns:
        str: The resulting ciphertext or plaintext.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            if mode == 'encrypt':
                new_index = (index + shift) % 26
            elif mode == 'decrypt':
                new_index = (index - shift) % 26
            result += alphabet[new_index]
        else:
            result += char  # Preserve non-alphabetic characters

    return result

def main():
    direction = input("Type 'encrypt' to encrypt, or 'decrypt' to decrypt: ").lower()
    user_text = input("Type your message: ")
    shift_value = int(input("Type the shift number: "))

    if direction == 'encrypt':
        encrypted_text = caesar_cipher(user_text, shift_value, mode='encrypt')
        print(f"The encrypted text is: {encrypted_text}")
    elif direction == 'decrypt':
        decrypted_text = caesar_cipher(user_text, shift_value, mode='decrypt')
        print(f"The decrypted text is: {decrypted_text}")
    else:
        print("Invalid input. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
