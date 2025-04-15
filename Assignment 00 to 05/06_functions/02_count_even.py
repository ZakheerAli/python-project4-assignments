# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the sum of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

def main():
    def count_even(my_list):
        count=0
        while True:
            user_input=input("Enter an integer or press enter to stop: ")
            if user_input == "":
                break
            user_input=int(user_input)
            my_list.append(user_input)
        
        for num in my_list:
            if num % 2 == 0:
                count+=1
        print(count)

    count_even([])

if __name__=="__main__":
    
    main()