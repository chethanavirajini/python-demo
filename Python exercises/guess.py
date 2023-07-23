# guessing game

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess_value = int(input("Guess: "))
    guess_count += 1
    if guess_value == secret_number:
        print("You won")
        break
else:
    print("Better luck next time")