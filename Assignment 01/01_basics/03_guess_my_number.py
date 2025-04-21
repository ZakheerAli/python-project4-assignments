# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random
def main():
    random_number=random.randint(0,99)
    print("I am thinking of a number between 0 and 99... ")
    while True:
        user_guess=int(input("Enter a guess: "))
        if user_guess == "":
            break
        if user_guess == random_number:
            print(f"Congrats! Your guess was correct.Number was {random_number}")
            break
        elif user_guess > random_number:
            print("Your guess is too high!")
        elif user_guess < random_number:
            print("Your guess is too low!")

if __name__=="__main__":
    main()
