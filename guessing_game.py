secret_word = input("Give the secret word: ")
guess = ""
guess_count = 0
guess_limit = 3

while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("Write your guess: ")
        guess_count += 1
        if guess != secret_word and guess_count != 3:
            print(f"Wrong answer, try again! Remaining guesses: {guess_limit - guess_count}")
        elif guess == secret_word:
            print("You win!")
    else:
        print("Out of guesses! You lose!")
        break
