#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur Mar 8 13:49:19 2023

FINAL SUBMISSION:

@authors: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt

Assumptions: 

1. The input message is a string containing only uppercase letters.
2. The input message does not contain any special characters, numbers, or whitespace.
        
Time Complexity:

The time complexity of the CaesarCipher implementation is O(n), where n is the length of the input message. 
This is because the _transform method iterates over each character in the message once and performs a constant number of operations on each character.
"""

class CaesarCipher:
    """Class for encryption and decryption using a Caesar cipher."""

    def __init__(self, shift):
        """Initialize Caesar cipher with a given integer shift for rotation."""
        encoder = [None] * 26  # temporary array for encryption
        decoder = [None] * 26  # temporary array for decryption
        for i in range(26):
            # compute and store the shifted alphabets for encryption and decryption
            encoder[i] = chr((i + shift) % 26 + ord('A'))
            decoder[i] = chr((i - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)  # store the encryption alphabets as a string
        self._backward = ''.join(decoder)  # store the decryption alphabets as a string

    def encrypt(self, message):
        """Encrypt a message using the stored shift value."""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Decrypt a secret message using the stored shift value."""
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Transform a message based on the given code string."""
        message_list = list(original)
        for i in range(len(message_list)):
            if message[i].isupper():
                # shift the uppercase letters based on the given code string
                k = ord(message_list[i]) - ord('A')
                message_list[i] = code[k]
        return ''.join(message_list)



cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
coded = cipher.encrypt(message)
print('Encrypted message:', coded)
answer = cipher.decrypt(coded)
print('Decrypted message:', answer)

# run some test cases to check the functionality of the cipher
assert coded == "WKH HDJOH LV LQ SODB; PHHW DW MRH'V."
assert answer == "THE EAGLE IS IN PLAY; MEET AT JOE'S."
