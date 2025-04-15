import math

# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!


# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Here's a sample run of the program (user input is in bold italics):

# Enter the length of AB: 3

# Enter the length of AC: 4

# The length of BC (the hypotenuse) is: 5.0








def main():
    length_of_perp_AB=float(input("Enter the length of side AB : "))
    length_of_base_AC=float(input("Enter the length of side AC : "))
    sum_of_square_of_AB_and_AC=(length_of_perp_AB ** 2) + (length_of_base_AC ** 2)
    length_of_hyp_BC = math.sqrt(sum_of_square_of_AB_and_AC)
    print(f"The length of hypoteneous BC is \033[1;3m{length_of_hyp_BC}\033[0m")

if __name__=="__main__":
    main()