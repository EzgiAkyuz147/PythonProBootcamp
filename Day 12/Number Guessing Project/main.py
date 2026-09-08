import art, random
print(art.logo)
print("Welcome to Number Guessing Project!")
print("I am thinking of a number between 1 and 100.")
level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
num = random.randint(1, 100)
attempts = 0
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("You entered an invalid level. Please try again.")
print(f"You have {attempts} remaining to guess the number!")

def difference(my_choice, number):
    if my_choice < number:
        print("Too low")
        return False
    elif my_choice > number:
        print("Too high")
        return False
    else:
        print(f"You guessed correctly :) The answer was {my_choice}")
        return True

while attempts > 0:
    guess = int(input("Make a guess: "))
    result = difference(guess, num)
    if result:
        break
    attempts = attempts - 1
    print(f"You have {attempts} remaining to guess the number!")

