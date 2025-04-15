# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

def main():
    number=float(input("Enter a number to see its square:  "))
    square=float(number**2)
    print(f"The square of {number} is \033[1m {square} \033[0m")
    
if __name__=="__main__":
    main()