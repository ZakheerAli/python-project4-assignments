# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(my_list):
    print(my_list[len(my_list) - 1])

def get_last():
    my_list=[]
    user_input=input("Enter an element to add in a list and press enter to stop: ")
    while user_input != "":
        my_list.append(user_input)
        user_input=input("Enter an element to add in a list and press enter to stop: ") 
    return my_list

def main():
    my_list=get_last()
    get_last_element(my_list)
    

if __name__=="__main__":

    main()