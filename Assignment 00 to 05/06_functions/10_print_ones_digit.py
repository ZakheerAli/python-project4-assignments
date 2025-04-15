# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

# Here's a sample run (user input is in blue):

# Enter a number: 42 The ones digit is 2

def print_ones_digit(num):
    ones_digit=num % 10
    return ones_digit

def main():
    user_number=int(input("\033[94mEnter a number: \033[0m"))
    result = print_ones_digit(user_number)
    print(f"The Ones digit of {user_number} is {result}")

if __name__=="__main__":
    main()