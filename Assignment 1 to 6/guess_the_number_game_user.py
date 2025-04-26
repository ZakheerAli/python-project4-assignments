import random

def main():
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")

    random_num = random.randint(1, 100)
    attempt = 0

    while True:
        user_guess = input("Enter your guess (or press Enter to quit): ")
        
        if user_guess == "":
            print("🚪 You exited the game. Goodbye!")
            break

        try:
            user_guess = int(user_guess)
            attempt += 1
        except ValueError:
            print("❌ Invalid input. Please enter a number.\n")
            continue

        if user_guess > random_num:
            print("📈 Too high! Try again.\n")
        elif user_guess < random_num:
            print("📉 Too low! Try again.\n")
        else:
            print(f"🎉 Congratulations! You guessed it right. The number was {random_num}.")
            print(f"🧠 It took you {attempt} attempt(s). Well done!\n")
            break

if __name__ == "__main__":
    main()
