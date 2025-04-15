# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.


def main():
    Anton:int = 21
    Beth:int = Anton + 6
    Chen:int = Beth + 20
    Drew:int = Chen + Anton
    Ethan:int = Chen 

    print(f"Anton is {Anton} year old")
    print(f"Beth is {Beth} year old ")
    print(f"Chen is {Chen} year old")
    print(f"Drew is {Drew} year old")
    print(f"Ethan is {Ethan} year old")

if __name__=="__main__":
    main()