#!/usr/bin/env python3

"""
Program that asks the user for a word then converts it to pig latin. It will ask
the user if they want to do it again and will continue until user inputs N
"""

CONSONANTS = "bcdfghjklmnpqrstvwxwz"
VOWELS = "aeiou"

def pig_latin(word: str) -> str:
    """
    Function to take a string and convert it to piglatin
    
    Args:
        word (string): users input

    Returns: 
        string: word in pig latin
    """
    # bug fix to the code on github. If user inputs a consonant it will
    # loop forever and break

    if len(word) == 1 and word in CONSONANTS:
        return word + "ay"
    
    while word[0].lower() == "y":
        word = word[1:] + word[0]

    if word[0].lower() in CONSONANTS:
        while word[0].lower() in CONSONANTS:
            word = word[1:] + word[0]
        word += "ay"
    elif word[-1] == "y":
        word += "ay"
    else:
        word += "yay"

    return word


if __name__ == "__main__":

    while True:
        print("Give me a word and I will translate it into pig latin for you.")
        user_word = input("Please enter a word: ")

        print(pig_latin(user_word))
        decision = input("Would you like to continue? (Enter Y or N): ")
        decision = decision.upper()

        if decision != "Y":
            break