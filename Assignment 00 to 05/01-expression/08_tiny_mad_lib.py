# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!


# Here's a sample run (user input is in bold italics):
# Please type an adjective and press enter. tiny
# Please type a noun and press enter. plant
# Please type a verb and press enter. fly
# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

def main():
    adjective=input("Please type an adjective and press enter:  ")
    noun=input("Please type a noun and press enter:  ")
    verb=input("Please type a verb and press enter:  ")
    print(f"My {adjective} {noun} just tried to {verb}")
if __name__=="__main__":
    main()