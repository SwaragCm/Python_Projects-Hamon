
import random
# with the help of sleep funtion in the time module we can delay some programs..
from time import sleep

# This function will return the list having the hangman parts,
def print_hangman():
    hangman_parts = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    
    return hangman_parts


# This function welcomes the player, prompts them to start,
#  selects a random word for the game, and begins the guessing process. If the player declines to start, the game quits.
def start():
    # Assigning print_hangman() function (which returns the list includes the hangman parts) to a variable
    hangman = print_hangman()    
    
    # looping through the list, used sleep to give the effect of animation
    for part in hangman:
        print(part)
        sleep(0.1) 

    # These lines print out introductory messages
    print("HangMan  ")
    print("Welcomes You To The World Of Words !!!")
    print("Ready To Guess ??? (y/n)")
    user = input("> ")

    if user == "y":
        # This line calls the dictionary_words() to get a random word from a dictionary file 
        word = dictionary_words("dictionary.txt").lower()

        # This line calls the handle_player_guess() to start the game with the selected word.
        handle_player_guess(word)        
    else:
        quit()



# This function will return the random word from the list, which was inside a file.
def dictionary_words(dictionary_file):
        
        file = open(dictionary_file)
        words = file.read()
        words = words.split()
       
        # It creates a new list (guess_words) consisting only of words without apostrophes
        guess_words = [word for word in words if "'" not in word]

        # Here i used random.choice, It is used to choose a random element from this list,
        return random.choice(guess_words) if guess_words else None


# this function handles the player's guesses, updates the game state accordingly, and determines the outcome of the Hangman game.
def handle_player_guess(word):
    hangman = print_hangman()
    chance = 6
    
    # This line creates a list named word_mask consisting of dashes (-) to represent the hidden letters of the word. 
    # The length of the list is the same as the length of the word to be guessed.
    word_mask = list("-" * len(word))

    # This will keep track of the characters already guessed by the player.
    guessed_characters = []
    
    print(" ".join(word_mask))

    # This line initiates a while loop that continues as long as there are still letters to be guessed in the word 
    while "-" in word_mask: 
        user_input = input("Enter the word ")

        # This line checks if the guessed letter has already been guessed by the player by looking for it in the list.
        if user_input in guessed_characters:
            print("You've already guessed this letter. Try again.")
            chance -= 1
            print("Chances remaining:", chance)
            if chance == 0:
                print("You Loose, TRY AGAIN !!!")
                print(hangman[-1])
                sleep(1)
                return start()
            else:
                print(hangman[6 - chance])            
        
        guessed_characters.append(user_input)
        
        correct_guess = False
        
        # this loop iterates through each character in the word to be guessed. 
        for i in range(len(word)):
            # If the player's guessed letter matches any of the characters in the word,
            if user_input == word[i]:
                correct_guess = True
                # this will replace the dash(-) in the list with the letter user guessed
                word_mask[i]=user_input
                              
        
        if not correct_guess:
            print("Character not found in the word. Try again.")
            chance -=1
            print("chance is remaining",chance)

            # If the player has no more chances left, they lose the game. The hangman is fully displayed, and re-start.
            if chance == 0:
                print("You Loose, TRY AGAIN !!!")
                print(hangman[-1])
                sleep(1)
                return start()                               
            else:
                # player still has chances remaining, the corresponding part of the hangman is displayed based on the remaining chances.
                print(hangman[6 - chance])
            
        else:
            print(" ".join(word_mask))

# Once all letters in the word have been guessed correctly, the player wins. A congratulatory message is printed, and the game restarts.
    print("Congratulations! You guessed the correct word:", "".join(word_mask))
    sleep(1.5)
    start()               
            

if __name__ == '__main__':
    start()
