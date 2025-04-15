# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.

# Here's a sample run of the program (user input in bold italics):

# Enter a number: 2 Double that is 4
def double(num):
    return num * 2

def main():
    num = int(input("\033[1;3mEnter a number: \033[0m"))
    result=double(num)
    print(f"Double of {num} is {result}")

if __name__=="__main__":
    main()

