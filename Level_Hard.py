def hard(num):
    for attempts_left in range(5,0,-1):
        print(f"You have {attempts_left} attempts left to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == num:
            print(f"You got it! The number was {num}.")
            break
        elif guess > num:
            print("Too high.")
            print("Guess again.")

        else:
            print("Too low.")
            print("Guess again.")
    else:
        print("You run out of guesses.")