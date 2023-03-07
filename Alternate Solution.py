def caesar_cipher(input_string, shift):
    output_string = ""
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the appropriate ASCII offset for the character (uppercase or lowercase)
            if char.isupper():
                offset = ord('A')
            else:
                offset = ord('a')
            # Apply the shift to the character using the formula (i + r) mod 26
            shifted_index = (ord(char) - offset + shift) % 26
            # Convert the shifted index back into a character and add it to the output string
            output_string += chr(shifted_index + offset)
        else:
            # If the character is not a letter, add it to the output string unchanged
            output_string += char
    return output_string

def caesar_decipher(input_string, shift):
    return caesar_cipher(input_string, -shift)

coded = caesar_cipher("The Eagle is in Play; Meet at Joe's", 5)
print("Secret: ", coded)

answer = caesar_decipher(coded,5 )
print("Message: ", answer)

