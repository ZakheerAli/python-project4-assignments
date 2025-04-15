# In this program we show an example of using dictionaries to keep track of information in a phonebook.


def read_phone_number():
    phonebook={}
    while True:
        name=input("Enter your Name: ")
        if name =="":
            break
        number=input("Enter your number: ")
        if number == "":
            break
        phonebook[name]=number
    return phonebook


def print_name_and_number(phonebook):
    for i in phonebook:
        print(f"{i} --> {phonebook[i]}")

def find_name_and_number(phonebook):
    while True:
        find_name=input("Enter name to find: ")
        if find_name in phonebook:
            print(f"{find_name} --> {phonebook[find_name]}")
        else:
            print(f"Sorry we could not find {find_name} !")

def main():
    phonebook=read_phone_number()
    print_name_and_number(phonebook)
    find_name_and_number(phonebook)

if __name__=="__main__":
    main()