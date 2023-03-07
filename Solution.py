"""
authors (Github handles): Paul Sharrat (psharratt), Amin Oueslati (amin-oueslati), Fabian Metz (Fabian-Metz), Oskar Krafft (OskarKrafft)
"""

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26
        
    def encrypt(self, message):
        """
        Encrypts a message using the Caesar Cipher encryption algorithm.
        """
        char_list = list(message)
        
        for i in range(len(char_list)):
            if char_list[i].isalpha():
                if char_list[i].isupper():
                    char_list[i] = self.shift_character(char_list[i], 'A')
                elif char_list[i].islower():
                    char_list[i] = self.shift_character(char_list[i], 'a')
        
        encrypted_message = self.list_to_string(char_list)
        return encrypted_message
        
    def decrypt(self, message):
        """
        Decrypts a message using the Caesar Cipher encryption algorithm.
        """
        char_list = list(message)
        
        for i in range(len(char_list)):
            if char_list[i].isalpha():
                if char_list[i].isupper():
                    char_list[i] = self.shift_character(char_list[i], 'A', reverse=True)
                elif char_list[i].islower():
                    char_list[i] = self.shift_character(char_list[i], 'a', reverse=True)
        
        decrypted_message = self.list_to_string(char_list)
        return decrypted_message
    
    def shift_character(self, char, base_char, reverse=False):
        """
        Shifts a single character by the specified amount, either forwards or backwards.
        """
        if reverse:
            shift = -self.shift
        else:
            shift = self.shift
            
        char_code = ord(char) - ord(base_char)
        shifted_code = (char_code + shift) % 26
        shifted_char = chr(shifted_code + ord(base_char))
        return shifted_char
    
    def list_to_string(self, char_list):
        """
        Converts a list of characters back to a string.
        """
        return ''.join(char_list)


# Sample Test

cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
coded = cipher.encrypt(message)
print("Secret: ", coded)
answer = cipher.decrypt(coded)
print("Message: ", answer)