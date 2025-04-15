# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() and check if it returns True or not. If done() returns True, we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), which will print "I'm done.". We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.

# Here's a sample run of this program:

# I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.


import random  # Ye module random numbers generate karne ke liye use hota hai

# Ye variable define karta hai ke kitna chance hai done() function ke True hone ka
DONE_LIKELIHOOD = 0.2  # 20% chance hai ke counting ruk jaaye

# Ye helper function decide karta hai ke counting ko stop karna hai ya nahi
def done():
    return random.random() < DONE_LIKELIHOOD  # Agar random number 0.2 se chhota hua, to return True

# Ye function 1 se 10 tak count karta hai, lekin beech me randomly ruk sakta hai
def chaotic_counting():
    for i in range(1, 11):  # 1 se 10 tak loop chalega
        if done():  # Har number se pehle check karega ke kya rukna hai
            return  # Agar done() True ho gaya, to function yahin pe ruk jaayega (exit ho jaayega)
        print(i)  # Agar done() False hai to number print hoga

# Ye main function program ka starting point hai
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Yahan se counting start hoti hai
    print("I'm done.")  # Jab chaotic_counting() khatam hota hai, to ye line print hoti hai

# Ye condition ensure karti hai ke main() sirf tab chale jab file direct run ho
if __name__ == "__main__":
    main()
