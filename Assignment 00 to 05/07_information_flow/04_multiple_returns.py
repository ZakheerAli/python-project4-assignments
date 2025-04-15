# There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

# To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:

# Asks the user for their first name and stores it in a variable

# Asks the user for their last name and stores it in a variable

# Asks the user for their email address and stores it in a variable

# Returns all three of these pieces of data in the order it was asked

# You can return multiple pieces of data by separating each piece with a comma in the return line.

# Here is an example run of the program:

# What is your first name?: Jane

# What is your last name?: Stanford

# What is your email address?: janestanford@stanford.edu

# Received the following user data: ('Jane', 'Stanford', 'janestanford@stanford.edu')

# (Note. This idea is called tuple packing/unpacking. We "pack" our return values into a single data structure called a tuple. We can then "unpack" these values back into our original values or leave them as a tuple.)

def get_user_data():
    user_first_name=input("What is your first name?  ")
    user_last_name=input("What is your last name?  ")
    user_email=input("What is your Email address?  ")
    return user_first_name , user_last_name ,user_email

def main():
    result = get_user_data()
    print(f"Received the following user data: \033[93m{result}\033[0m")

if __name__=="__main__":
    main()
     