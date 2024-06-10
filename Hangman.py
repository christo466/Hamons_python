import random  # Import the random module for random word selection and random operations
import sys     # Import the sys module to handle system-specific parameters and functions

def hang_man(error, word_list, temporary_list, chance, random_word, temporary_list_word):
    """
    Display the current hangman stage based on the number of errors and check if the player has won.

    Parameters:
    - error: Number of incorrect guesses
    - word_list: The list of characters in the target word
    - temporary_list: The list of guessed characters (with underscores for unguessed letters)
    - chance: The number of remaining chances
    - random_word: The word the player is trying to guess
    - temporary_list_word: The current guessed word as a string
    """
    # Hangman stages depicting the state of the game based on the number of wrong guesses
    hangman_stages = [
        r"""
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ---------
        """,
        r"""
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ---------
        """,
    ]

    # Check if the player has guessed the word correctly and won the game
    if random_word == temporary_list_word:
        game_won(temporary_list_word)  # Call game_won function to handle winning
    elif random_word != temporary_list_word:
        print(hangman_stages[error])  # Display the current hangman stage
        # Prompt the player to continue guessing
        print_the_gues(word_list, temporary_list, chance)

def game_won(temporary_list_word):
    """
    Handle the scenario when the player wins the game.

    Parameters:
    - temporary_list_word: The correctly guessed word
    """
    print("--------------------")
    print(f"The word: {temporary_list_word}")
    print("You have won the game")
    continue_playing()  # Ask the player if they want to continue playing

def lost_game(chance):
    """
    Handle the scenario when the player loses the game.

    Parameters:
    - chance: The number of remaining chances
    """
    if chance <= 0:
        print("You lost the game")
    print("Continue playing the game... yes or no")
    yes_or_no = input("> ")  # Get the player's input on whether to continue
    if yes_or_no == "yes":
        Main()  # Restart the game
    else:
        sys.exit(0)  # Exit the game if the player doesn't want to continue

def continue_playing():
    """
    Prompt the player to continue playing the game and handle their response.
    """
    print("Continue playing the game... yes or no")
    yes_or_no = input("> ").lower()  # Get the player's input and convert it to lowercase
    if yes_or_no == "yes":
        Main()  # Restart the game
    else:
        sys.exit()  # Exit the game

def check_chance(chance, word_list, temporary_list):
    """
    Check the remaining chances and proceed accordingly.

    Parameters:
    - chance: The number of remaining chances
    - word_list: The list of characters in the target word
    - temporary_list: The list of guessed characters (with underscores for unguessed letters)
    """
    print(f"Chances remaining: {chance}")
    if chance > 0:
        getting_word(word_list, temporary_list, chance)  # Prompt the player to guess another letter
    else:
        lost_game(chance)  # Handle the lost game scenario

def check_the_word(input_letter, word_list, temporary_list, chance):
    """
    Check if the guessed letter is in the word and update the state accordingly.

    Parameters:
    - input_letter: The letter guessed by the player
    - word_list: The list of characters in the target word
    - temporary_list: The list of guessed characters (with underscores for unguessed letters)
    - chance: The number of remaining chances

    Returns:
    - updated temporary_list, updated chance, random_word, updated temporary_list_word
    """
    length_of_word_list = len(word_list)
    random_word = "".join(word_list)  # Convert the word list to a string
    temporary_list_word = "".join(temporary_list)  # Convert the temporary list to a string

    if chance > 0:
        for i in range(length_of_word_list):
            if (input_letter == word_list[i] and input_letter != temporary_list[i]):
                temporary_list[i] = input_letter  # Update the temporary list with the guessed letter
                temporary_list_word = "".join(temporary_list)
                if random_word == temporary_list_word:
                    game_won(random_word)  # Handle winning scenario
                break
            elif (input_letter not in word_list):
                chance -= 1  # Decrease the chance if the guessed letter is not in the word
                break
            elif random_word.count(input_letter) == temporary_list_word.count(input_letter):
                chance -= 1  # Decrease the chance if the guessed letter is already guessed
                break

    return temporary_list, chance, random_word, temporary_list_word

def getting_word(word_list, temporary_list, chance):
    """
    Prompt the user to guess a letter and proceed with the game.

    Parameters:
    - word_list: The list of characters in the target word
    - temporary_list: The list of guessed characters (with underscores for unguessed letters)
    - chance: The number of remaining chances
    """
    input_letter = input("Enter the letter: ")  # Get the player's guessed letter
    lower_letter = input_letter.lower()  # Convert the guessed letter to lowercase
    temporary_list, chance, random_word, temporary_list_word = check_the_word(lower_letter, word_list, temporary_list, chance)
    hang_man(6 - chance, word_list, temporary_list, chance, random_word, temporary_list_word)  # Display the hangman state and proceed

def gues_the_word(word):
    """
    Initialize the game state for a new word and start the game.

    Parameters:
    - word: The word the player is trying to guess
    """
    length_of_word = len(word)
    chance = 6  # Set the initial number of chances
    word_list = list(word.lower())  # Convert the word to a list of characters
    temporary_list = ["_"] * length_of_word  # Create a list of underscores representing the unguessed letters
    temporary_list_word = "".join(temporary_list)  # Convert the temporary list to a string
    hang_man(6 - chance, word_list, temporary_list, chance, word, temporary_list_word)  # Start the game
    getting_word(word_list, temporary_list, chance)  # Prompt the player to guess a letter

def print_the_gues(word_list, temporary_list, chance):
    """
    Display the current guessed state of the word and proceed with the game.

    Parameters:
    - word_list: The list of characters in the target word
    - temporary_list: The list of guessed characters (with underscores for unguessed letters)
    - chance: The number of remaining chances
    """
    print(f"Guess the word: {' '.join(temporary_list)}")  # Display the current guessed state of the word
    check_chance(chance, word_list, temporary_list)  # Check the remaining chances and proceed

def Random_word(words_list):
    """
    Select a random word from the list based on the chosen difficulty level.

    Parameters:
    - words_list: The list of words to choose from
    """
    level = input("> Choose the level: Easy = 1,  Medium = 2, Hard = 3: ")  # Prompt the player to choose a difficulty level
    if level in ["1", "2", "3"]:
        if level == "1":
            length_of_word = random.randint(1, 4)  # Easy level: word length between 1 and 4
        elif level == "2":
            length_of_word = random.randint(5, 8)  # Medium level: word length between 5 and 8
        elif level == "3":
            length_of_word = random.randint(9, 14)  # Hard level: word length between 9 and 14

        filtered_words = [word for word in words_list if len(word) == length_of_word]  # Filter words by chosen length
        random_word = random.choice(filtered_words)  # Select a random word from the filtered list
        gues_the_word(random_word)  # Start the game with the chosen word
    else:
        print("Give proper input")  # Prompt the player to provide a valid input
        Random_word(words_list)  # Retry the selection process

def remove_char_after_single_quote(words):
    """
    Remove characters following a single quote in the word list.

    Parameters:
    - words: The list of words to be cleaned
    """
    modified_words = []
    for word in words:
        if "'" in word:
            parts = word.split("'")
            modified_word = parts[0]  # Take the part before the single quote
            modified_words.append(modified_word)
        else:
            modified_words.append(word)
    Random_word(modified_words)  # Proceed with the filtered word list

def Main():
    """
    Main function to start the Hangman game. Reads words from a file and initializes the game.
    """
    file_path = "dictionary.txt"  # Specify the file path for the dictionary
    try:
        with open(file_path, 'r') as open_file:  # Open the dictionary file
            read_file = open_file.read()  # Read the file content
            words_list = read_file.split()  # Split the content into words
        remove_char_after_single_quote(words_list)  # Clean the words and start the game
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    Main()  # Entry point to start the Hangman game
