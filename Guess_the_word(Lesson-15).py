import random

words = ["apple", "banana", "cherry", "orange", "lemon"]
score = 0
num_attempts = 3

def print_progress(word, guessed_letters):
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

def check_word(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def get_hint(word):
    print(f"The word has {len(word)} letters.")

while True:
    print("Enter 1 to start or 2 to quit:")
    choice = input()

    if choice == "1":
        word = random.choice(words)
        guessed_letters = []

        print(f"You have {num_attempts} attempts to guess the word.")
        print_progress(word, guessed_letters)

        for i in range(num_attempts):
            print("Enter a letter or the whole word, or 'hint' to get a hint:")
            guess = input()

            if guess == "hint":
                get_hint(word)
                continue

            if guess == word:
                print("Congratulations, you guessed the word! You got +20 points!")
                score += 20
                break
            elif guess in guessed_letters:
                print("You already guessed this letter. Try again.")
                continue
            elif guess in word:
                print("Good guess! You got +10 points!")
                guessed_letters.append(guess)
                print_progress(word, guessed_letters)
                score += 10
            else:
                print("Wrong guess. Try again.")
        else:
            print("I'm sorry, but game over.")

    elif choice == "2":
        print("Your final score is:", score)
        break

    else:
        print("Invalid choice. Please enter 1 or 2.")