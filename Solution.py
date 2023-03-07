class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26
        
    def encrypt(self, message):
        
        # Convert message to list of characters
        char_list = list(message)
        
        # Encrypt each character by shifting it by self.shift
        for i in range(len(char_list)):
            if char_list[i].isalpha():
                if char_list[i].isupper():
                    char_list[i] = chr((ord(char_list[i]) - 65 + self.shift) % 26 + 65)
                elif char_list[i].islower():
                    char_list[i] = chr((ord(char_list[i]) - 95 + self.shift) % 26 + 95)
            else:
                char_list[i] = char_list[i]
        
        # Convert list of characters back to string
        encrypted_message = self.output(char_list)
        
        return encrypted_message
        
    def decrypt(self, message):
        
        # Convert message to list of characters
        char_list = list(message)
        
        # Decrypt each character by shifting it by -self.shift
        for i in range(len(char_list)):
            if char_list[i].isalpha():
                if char_list[i].isupper():
                    char_list[i] = chr((ord(char_list[i]) - 65 - self.shift) % 26 + 65)
                elif char_list[i].islower():
                    char_list[i] = chr((ord(char_list[i]) - 95 - self.shift) % 26 + 95)
            else:
                char_list[i] = char_list[i]
        
        # Convert list of characters back to string
        decrypted_message = self.output(char_list)
        
        return decrypted_message
    
    def output(self, char_list):
        
        # Convert list of characters back to string
        return ''.join(char_list)


# Test

cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
coded = cipher.encrypt(message)
print("Secret: ", coded)
answer = cipher.decrypt(coded)
print("Message: ", answer)