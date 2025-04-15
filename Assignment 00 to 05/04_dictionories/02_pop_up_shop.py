# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# How many (rambutan) do you want?: 1

# How many (mango) do you want?: 3

# Your total is $99.5

def main():
    my_fruits={
        "Mango" : 23,
        "Apple" : 12,
        "Banana" : 20,
        "Orange" : 10,    
        "Kiwi" : 8,
        "Grapes" : 14
        }
    total_price = 0

    for fruit in my_fruits:
        price=my_fruits[fruit]
        quantity=int(input(f"How many {fruit} do you want? "))
        total_price = total_price + (price * quantity)
    print(f"Your Total is ${total_price}")

if __name__=="__main__":
    main()