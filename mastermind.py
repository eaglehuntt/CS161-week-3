#!/usr/bin/env python3

"""
Mastermind game on the command line.
"""
import random

class MasterMindGame:
    
    def __init__(self):
        """
        Defines class variables.
        
        Args:
            self : instance of class 

        Returns:
            None
        """
        self.available_colors = ["A","B","C","D","E","F"]
        self.__secret_code = self.__get_secret_code()
        self.guesses_remaining = 12
        self.guessed_colors = []
        self.guessed_colors_correctness = []
        self.CODE_LENGTH = 4 # max length for a code is 4

    def play(self):
        """
        Initialzies game and prints game info.
        Also prints a key to understand corectness visual.
        
        Args:
            Self: instance of class

        Returns: 
            None
        """
        print('---------------')
        print('Mastermind Game')
        
        print('---------------')

        print('You are in a guessing match against the computer!')
        print('Find the secret combonation to win!')
        print("")
        print("Key:")
        print("X: A color is not in secret combo")
        print("O: A color in secret combo but misplaced")
        print("*: A color in seceret combo and correctly placed")
        print("")
        self.run_game()

    def __get_secret_code(self):
        """
        Randomizes the self.avaliable_colors array.
        It then returns a new array with a limit of 4.

        Args:
            Self: instance of class
        
        Returns: 
            New random array of 4 indexes.
        """
        return random.sample(self.available_colors, 4)
    
    def get_guess_correctness(self,user_guess_array):
        """
        This converts the guess (letters) into a viusal array (symbols).

        Args:
            self: guess
            user_guess_array: array of user input guesses (letters).

        Returns:
            A randomized orded of the user's guess array. This is so the user 
            does not get extra hints to which letter is correctly placed.
        """
        guess_correctness = []

        for color in user_guess_array:
            # check if guess is incorrect
            if color not in self.__secret_code:
                guess_correctness.append('X')
                
            # check if guess is fully correct 
            elif user_guess_array.index(color) == self.__secret_code.index(color):
                guess_correctness.append('*')

            # check if guess is kind of correct
            else:
                guess_correctness.append('O')

        return random.sample(guess_correctness,4)

    def did_win(self, guess_correctness):
        """
        Sets visual (symbols) as correct answer. Checks if user guess is correct
        And determines if user wins
        
        Args:
            self: instance of class
            guess_correctness: array that represents guess in degnated symbols.
            NOTE: symbol key printed before.
        
        Returns:
            True: if guess_correctness is equal to winning_array
        """
        winning_array = ["*","*","*","*"]
        if guess_correctness == winning_array:
            return True


    def run_game(self):
        """
        This will run the game. Asks for (letter) inputs based on avaliabe
        colors (they are listed).
        It will remove the already guessed color, to avoid same input.
        It will then append the guess into an array and display it as you go.
        It will determine if you win or lose and display end accordingly
        
        
        Has the logic built in to run game and output guesses remaing, arrays,
        and win/lose/try again prompts.

        Args:
            self: instance class

        Returns:
            None.

        """        
        
        while self.guesses_remaining >= 1: # while we can guess
            # user guess array is an array consisting of the colors the user
            # has guessed
            user_guess_array = []
            available_colors = ["A","B","C","D","E","F"]

            while len(user_guess_array) < self.CODE_LENGTH:
                user_color_guess = input(f'Available colors: {available_colors} \nEnter a color: ')
                print("")
                # set user guess to upper case.
                user_color_guess = user_color_guess.upper()
                
                # we need to make sure the user only selects colors available
                # and we need to make sure the user does not select the same
                # color twice
               
                if user_color_guess not in self.available_colors:
                    print('That color is not available to choose. try again')
                    print('')
                elif user_color_guess not in available_colors and user_color_guess in user_guess_array:
                    print('You already selected that color, try again.')
                    print('')
                else:
                    # we need to append the guessed color to the guess array,
                    # as well as remove the color from available guesses
                    user_guess_array.append(user_color_guess)
                    available_colors.remove(user_color_guess)
                    print(f'Your guess: {user_guess_array}')
                    print("")
                    
            # add the user's guess array to their guessed colors.
            # guessed colors is an array of previous guesses the user has made
            self.guessed_colors.append(user_guess_array)

            # guess correctness follows the key and informs the user how many
            # of their guesses are correctly placed
            guess_correctness = self.get_guess_correctness(user_guess_array)
            
            # add the user's guess to their guessed correctness array
            
            self.guessed_colors_correctness.append(guess_correctness)
            
            print("")
            print('Guess correctness: ')
            print("")
            print(guess_correctness[0], guess_correctness[1])
            print(guess_correctness[2], guess_correctness[3])
            print("")
            
            print('Previous guesses & how correct they were: ')
            for guess in self.guessed_colors:
                print(f"{guess} : {self.guessed_colors_correctness[self.guessed_colors.index(guess)]}")
            print("")
            
            if self.did_win(guess_correctness):
                print("You win")
                exit()
            else:
                self.guesses_remaining -= 1
                print(f"Guesses remaining: {self.guesses_remaining}")
                print("")

        print('You lose')
        print(f"Secret code: {self.__secret_code}")

game = MasterMindGame()
game.play()
