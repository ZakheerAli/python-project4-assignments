# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.
def count_num():
    dic={}
    while True:
        user_input=input("Enter a number: ")
        if user_input == "":
            break
        user_input=int(user_input)
        if user_input in dic:
            dic[user_input] += 1
        else:
            dic[user_input] = 1

    for num,count in dic.items():
        print(f"{num} appears {count} times")

def main():
    count_num()

if __name__=="__main__":
    main()

