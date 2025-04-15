# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

# Here's a sample run (user input is in blue):

# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12

def print_divisors(num):
    for i in range(num):
        iterator= i + 1 
        if num % iterator == 0:
            print(iterator)
def main():
    user_input=int(input("Enter a number: "))
    print_divisors(user_input)

if __name__=="__main__":
    main()
