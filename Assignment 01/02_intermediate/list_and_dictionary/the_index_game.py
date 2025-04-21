
# Problem #2: Index Game

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.


# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.
# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.

#  WAY 1...
def access_elem(lst , index):
    if 0 <= index < len(lst)  : #index >= 0 and index < len(lst)
        return lst[index]
    else:
        return "Your index is out of range!"
    
def modify_elem(lst,index,new_value):
    if 0 <= index < len(lst): # index >= 0 and index <  len(lst)
        lst[index]=new_value
        return lst 
    else:
        return "Your index is out of range!"

def slicing_elem(lst,start_index,end_index):
    if 0 <= start_index <= len(lst) and 0 <= end_index <= len(lst): #start_index >= 0 and start_index < len(lst) and end_index >= 0 and end_index < len(lst)
        return lst[start_index : end_index]
    else:
        return "Invalid input"


def index_game():
    lst=[1,2,3,4,5]
    print(f"Your current list = {lst}")
    print("Choose an operaion to perform on list :access, modify , slicing")
    operation = input("Enter operation: ").strip().lower()
    if operation == "access":
        index = int(input("Enter an index to access an element: "))
        print(access_elem(lst,index))
    elif operation == "modify":
        index=int(input("Enter an index to modify the element: "))
        new_value=input("Enter a new value to modify the list: ")
        print(modify_elem(lst , index , new_value))
    elif operation == "slicing":
        start_index=int(input("Enter a starting index: "))
        end_index=int(input("Enter an ending index: "))
        print(slicing_elem(lst,start_index, end_index))
    else:
        print("Invalid Input")

def main():
    index_game()

if __name__=="__main__":
    main()



# WAY 2..

def access_elem(lst,index):
    try:
        return lst[index]
    except IndexError:
        return "Your index is out of range"


def modify_elem(lst,index,new_value):
    try:
        lst[index] = new_value
        return lst
        
    except IndexError:
        return "your index is out of range"

def slicing_elem(lst,start_index,end_index):
    try:
        return lst[start_index:end_index]
        
    except IndexError:
        return "Your index is out of range"

def index_game():
    lst=[1,2,3,4,5]
    print(f"Current list: {lst}")
    print("Choose an operation to perform on list :access,modify,slicing")
    operation=input("Enter an operation: ").strip().lower()
    if operation == "access":
        index=int(input("Enter an index to access an element: "))
        print(access_elem(lst,index))
    elif operation == "modify":
        index=int(input("Enter an index to modify an element: "))
        new_value=input("Enter a new value to modify the list: ")
        print(modify_elem(lst,index,new_value))
    elif operation == "slicing":
        start_index=int(input("Enter a starting index: "))
        end_index=int(input("Enter an Ending index: "))
        print(slicing_elem(lst,start_index ,end_index))
    else:
        print("Invalid input!")
    
def main():
    index_game()

if __name__=="__main__":
    main()

