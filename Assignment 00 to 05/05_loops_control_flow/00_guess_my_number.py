# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random
def main():

    random_number=random.randint(0,99)
    print("I am thinking of a number between 0 to 99...")
    while True:
        user_guess=input("Enter a guess:  ")
        if user_guess == "":
            break
        user_guess=int(user_guess)
        if user_guess == random_number:
            print(f"Congrats! You guess was right. Number was {random_number}")
            break
        elif user_guess > random_number:
            print("Your guess is too high")
        elif user_guess < random_number:
            print("Your guess is too low")

if __name__=="__main__":
    main()