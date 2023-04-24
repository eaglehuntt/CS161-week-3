#!/usr/bin/env python3

"""
Script to get user inputs then encrypt them with a key.
"""
UNICODE_LOWER_A = 97
UNICODE_LOWER_Z = 122

UNICODE_UPPER_A = 65
UNICODE_UPPER_Z = 90

ALPHABET_LOWER_CASE = list(map(chr, range(UNICODE_LOWER_A, UNICODE_LOWER_Z + 1)))
ALPHABET_UPPER_CASE = list(map(chr, range(UNICODE_UPPER_A, UNICODE_UPPER_Z + 1)))

USER_STRING = input('Enter string to encrypt: ')
KEY = int(input('Enter key: '))


def get_encrypted_index(index, key):
    """
    If the index value would be greater than 26
    We loop around until the new value is < 26.
    Args:
        index (int): Index of letter in alphabet array.
        key (int): number to shift letter by.

    Returns:
        int: new encrypted value that is within alphabet range.
    """
    # incriment index by key which is basically encrypting but were just storing
    # the index int at this point

    new_index = index + key
    max_length = 26

    while new_index >= max_length:
        new_index -= max_length
    return new_index

def get_encrypted_letter(letter, key, is_upper):
    """
    Takes a letter and finds the original index in our alphabet arrays,
    adds the key to that index, then returns the alphabet array at the new
    encrypted index. 

    Args:
        letter (string): letter to encrypt
        key (int): number to shift letters by
        is_upper (bool): flag to check if letter is upper case or not.

    Returns:
        (string): the letter the original index was + the key
    """

    if is_upper:
        original_index = ALPHABET_UPPER_CASE.index(letter)
        encrypted_index = get_encrypted_index(original_index, key)
        return ALPHABET_UPPER_CASE[encrypted_index]
    else:
        original_index = ALPHABET_LOWER_CASE.index(letter) # 25
        encrypted_index = get_encrypted_index(original_index, key)
        return ALPHABET_LOWER_CASE[encrypted_index]

def encrypt_string(user_string, key):
    """
    All characters get verified if part of alphabet.
    If they aren't its just added to the encrypted_array.
    If it is a letter, it gets identified as upper or lower.
    Then appended to the encypted array and shifted (based on key #)
    Finally it converts the array into a string and returns it.

    Args:
        user_string (string): gets user decrypted text.
        key (int): determines shift value.
    
    Returns:
        (string) : Encrypted text
    """
    user_input_as_array = list(user_string)
    encrypted_message_as_array = []

    for character in user_input_as_array:
        if not character.isalpha():
            encrypted_message_as_array.append(character)

        elif character == character.upper():
            encrypted_message_as_array.append(get_encrypted_letter(character,key,True))

        else:
            encrypted_message_as_array.append(get_encrypted_letter(character,key,False))
    return ''.join(encrypted_message_as_array)

print(encrypt_string(USER_STRING,KEY))
