# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

def get_first_elem(lst):
    print(lst[0])
    print(lst)

def get_first():
    lst=[]
    user_input=input("Enter an element to add in a list and press enter to stop: ")
    while user_input != "":
        lst.append(user_input)
        user_input=input("Enter an element to add in a list and press enter to stop: ")
    
    return lst

def main():
    lst=get_first()
    get_first_elem(lst)

if __name__=="__main__":
    main()
