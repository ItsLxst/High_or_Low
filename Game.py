import random
import Level_Easy
import Level_Hard


print("Welcome to High or Low!")
num = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == "easy":
    Level_Easy.easy(num)
elif level == "hard":
    Level_Hard.hard(num)
else:
    print("Not a valid level.")