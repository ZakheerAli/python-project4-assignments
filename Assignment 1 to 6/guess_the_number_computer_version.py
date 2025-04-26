def main():
    print("🤖 Think of a number between 1 to 100 (but don't tell me!)")
    print("✅ I'll try to guess it.")
    print("🗣️ Just reply with: 'higher', 'lower', or 'correct'")
   
    low=1
    high=100
    attempt=0
    while low <= high:
        attempt += 1
        computer:int=(low + high) // 2
        print(f"Is your number {computer}")
        user_guess=input("Enter a guess (higher/lower/correct): ").strip().lower()
        if user_guess=="higher":
            low= computer + 1
        elif user_guess == "lower":
            high=computer - 1
        elif user_guess == "correct":
            print(f"\n🎉 Yay! I guessed your number in {attempt} tries!")
            break
        else:
            print("❌ Invalid input. Please type: higher, lower, or correct.")


if __name__=="__main__":
    main()