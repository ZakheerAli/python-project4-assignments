import random
def main():
    words=["apple","mango","orange","banana","watermelon","strawberry"]
    random_word=random.choice(words)
    display = ["_"] * len(random_word)
    wrong_guess=0
    max_guess=6

    while "_" in display and wrong_guess < max_guess:
        print(f"Current Word = {" ".join(display)}")
        user_guess=input("Enter a guess : ").strip().lower()
        if len(user_guess) == 1 and user_guess.isalpha():
            pass
        else:
            print("❌Invalid Input!")
            continue
        if user_guess in random_word:
            for i in range(len(random_word)):
                if random_word[i]==user_guess:
                    display[i] = user_guess
            print(f"✅ Correct Guess")
        else:
            wrong_guess+=1
            print("❌ Wrong guess")

    if "_" not in display:
         print("\n🎉 Congratulations! You guessed the word:", random_word)
    else:
        print("\n💀 Game Over! The word was:", random_word)
            

if __name__=="__main__":
    main()





# import random
# def main():
#     words=["pakistan","india","german","france","america","dubai"]
#     word=random.choice(words)
#     display=["_"] * len(word)
#     wrong_guess=0
#     turns=6

#     while "_" in display and wrong_guess < turns:
#         print(f"Current word = {" ".join(display)}")
#         guess=input("Enter a guess: ").strip().lower()
#         if len(guess) == 1 and guess.isalpha():
#             pass
#         else:
#             print("invalid Input!")

#         if guess in word:
#             for i in range(len(word)):
#                 if word[i] == guess:
#                     display[i]=guess
#             print("Correct Guess")
#         else:
#             wrong_guess+=1
#             print("Wrong Guess")
    
#     if "_" not in display:
#         print(f'Your guess was right ,The word was {word}')
#     else:
#         print(f"You guess was wrong .The word was {word}")

# if __name__=="__main__":
#     main()




