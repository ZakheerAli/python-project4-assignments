import random
def main():
    num_round:int = 5
    score = 0
    print("\n🎮 Welcome to the High-Low Guessing Game! 🎯")
    print("========================================")
    print("In each round, you'll see your number.")
    print("Try to guess whether your number is HIGHER or LOWER than the computer's hidden number.")
    print("You earn a point for every correct guess!")
    print("----------------------------------------")
    for i in range(1,num_round + 1):
        your_num=random.randint(1,100)
        computer_num=random.randint(1,100)
        print(f"\n🔁 Round {i} of {num_round}")
        print(f"🔢 Your number is: {your_num}\n")


        guess:str=input("Do you think your number is higher or lower than computer's number:  ")
        guess=guess.strip().lower()

        if guess == "higher" and your_num > computer_num:
            print(f"✅ Correct! The computer's number was {computer_num}. Well done! 🎉")
            score+=1
        elif guess == "lower" and your_num < computer_num:
            print(f"✅ Correct! The computer's number was {computer_num}. Great job! 🚀")
            score+=1
        elif guess in ["higher" , "lower"]:
            print(f"❌ Incorrect. The computer's number was {computer_num}")
        else:
             print("⚠️ Invalid input. Please enter only 'higher' or 'lower'.")
           
        print(f"🎯 Your current score is: {score}")
    else:
        print("\n🏁 Game Over!")
        print(f"🏆 Your final score is: {score} out of {num_round}")


if __name__=="__main__":
    main()








