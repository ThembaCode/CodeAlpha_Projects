import random

def select_random_word():
    words = ['python', 'hangman', 'programming', 'data', 'science', 'openai', 'machine', 'learning']
    return random.choice(words)

# Hangman Guessing Game
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nSorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()


