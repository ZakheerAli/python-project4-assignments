import random
# Simulate rolling two dice, and prints results of each roll as well as the total.  
 
def main():

    dice1=random.randint(1,6)
    dice2=random.randint(1,6)

    print(f"The sum of  first die {dice1} and second die {dice2} is {dice1 + dice2}")
if __name__=="__main__":
    main()