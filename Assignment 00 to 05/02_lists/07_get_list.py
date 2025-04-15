# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']
def print_full_list(my_list):
    print(my_list)


def get_full_list():
    my_list=[]
    user_input=input("Enter a value and press enter to stop: ")
    while user_input != "":
        my_list.append(user_input)
        user_input=input("Enter a value and press enter to stop: ")
    return my_list

def main():
    my_list=get_full_list()
    print_full_list(my_list)

if __name__=="__main__":
    main()