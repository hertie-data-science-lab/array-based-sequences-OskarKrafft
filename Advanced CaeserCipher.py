#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur Mar 9 15:45:23 2023

FINAL SUBMISSION:

@authors: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt

Assumptions: 

1. The input message does not contain any special characters, numbers, or whitespace.
2. The encryption and decryption keys are generated randomly for each instance of the CaesarCipher class. That means that the same key will not be used for any two messages.

        
Time Complexity:

The time complexity of the CaesarCipher implementation is O(n), where n is the length of the input message. 
This is because the _transform method iterates over each character in the message once and performs a constant number of operations on each character.
"""


import random

class CaesarCipherAdvanced:
    """Class for encryption and decryption using a Caesar cipher."""

    def __init__(self):
        """Construct Caesar cipher with a random shift value for rotation."""
        self.shift = random.randint(1, 25)  # generate random shift value
        encoder_upper = [None] * 26  # temp array for uppercase encryption
        decoder_upper = [None] * 26  # temp array for uppercase decryption
        encoder_lower = [None] * 26  # temp array for lowercase encryption
        decoder_lower = [None] * 26  # temp array for lowercase decryption
        for k in range(26):
            encoder_upper[k] = chr((k + self.shift) % 26 + ord('A'))
            decoder_upper[k] = chr((k - self.shift) % 26 + ord('A'))
            encoder_lower[k] = chr((k + self.shift) % 26 + ord('a'))
            decoder_lower[k] = chr((k - self.shift) % 26 + ord('a'))
        self._forward_upper = ''.join(encoder_upper)  # uppercase encoding key
        self._backward_upper = ''.join(decoder_upper)  # uppercase decoding key
        self._forward_lower = ''.join(encoder_lower)  # lowercase encoding key
        self._backward_lower = ''.join(decoder_lower)  # lowercase decoding key

    def encrypt(self, message):
        """Return string representing encrypted message."""
        return self._transform(message, self._forward_upper, self._forward_lower)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self._transform(secret, self._backward_upper, self._backward_lower)

    def _transform(self, original, code_upper, code_lower):
        """Transform a message based on the given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index from 0 to 25
                msg[k] = code_upper[j]  # replace uppercase character
            elif msg[k].islower():
                j = ord(msg[k]) - ord('a')  # index from 0 to 25
                msg[k] = code_lower[j]  # replace lowercase character
        return ''.join(msg)

cipher = CaesarCipherAdvanced()
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
coded = cipher.encrypt(message)
print('Secret: ', coded)
answer = cipher.decrypt(coded)
print('Message:', answer)