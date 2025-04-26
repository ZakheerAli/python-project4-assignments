import random
def main():
    print("\n🎮WELCOME TO THE ROCK ,PAPER AND SCISSOR GAME")
 
    user=input("What is your choice ? 👊 r for rock ,📄 p for paper and ✌ s for scissor:\n").strip().lower()
    emoji={"r":"👊 ROCK" , "p":"📄 PAPER" ,"s":"✌ SCISSOR"}
    if user in ["r","p","s"]:
        print(f"Your choice {emoji[user]} ")
    else:
        print("invalid input")
        return

    computer=random.choice(["r","p","s"])
    print(f"Computer choice {emoji[computer]}")
    if user == computer:
        print("draw\n ")
    elif (user =="r" and computer=="s") or (user == "s" and computer=="p") or (user=="p" and computer=="r"):
        print("🎉Congratulation! You Won\n")
    else:
        print("Try again! Computer Won\n")


if __name__=="__main__":
    main()

