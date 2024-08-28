import random
from randomwords import country_names  # Importing the list of country names from the module

print("Guess the country Name")
# Set up initial variables
word_list = country_names  # List of possible words to guess
lives = 6  # Number of incorrect guesses allowed
choosen_word = random.choice(word_list).lower()  # Randomly choose a word and convert it to lowercase
# print(choosen_word)  # Print the chosen word for testing purposes (remove or comment this out in the final version)

# Create the initial placeholder for the word (e.g., "_____" for a 5-letter word)
placeholder = "_" * len(choosen_word)
print(placeholder)  # Display the initial placeholder

game_over = False  # Flag to indicate if the game is over
correct_letters = []  # List to track correctly guessed letters

# Main game loop
while not game_over:    
    guess = input("Guess a letter: ").lower()  # Get the player's guess and convert it to lowercase

    # Build the display string based on the current state of guessed letters
    display = ""
    for letter in choosen_word:
        if letter == guess:
            display += letter  # Add the guessed letter if it's correct
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter  # Add the letter if it was already guessed correctly
        else:
            display += "_"  # Add a placeholder for unguessed letters

    # Check if the guess was incorrect
    if guess not in choosen_word:
        lives -= 1  # Decrease the number of lives
        print(f"Incorrect! You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print(f"Game Over! The word was '{choosen_word}'.")

    # Display the current state of the word
    print(display)

    # Check if the player has won
    if "_" not in display:
        game_over = True
        print("You win!")

# Final game message
if "_" not in display:
    print(f"Congratulations! You correctly guessed the word: '{choosen_word}'")
else:
    print(f"Better luck next time! The word was '{choosen_word}'.")
