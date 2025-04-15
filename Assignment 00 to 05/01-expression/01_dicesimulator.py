# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works

import random
def dice():
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    total=die1 + die2
    print(f"The sum of first dice {die1} and second dice {die2} is {total}")

def main():
    die1:int=10
    print(f"die1 in main function is {die1}")
    dice()
    dice()
    dice()
    die2:int =20
    print(f"die2 in main function is {die2}")

if __name__=="__main__":
    main()