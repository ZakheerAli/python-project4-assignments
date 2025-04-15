# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

def main():
    mass = float(input("Enter the mass in kg: "))
    c_speed_of_light = 299792458 
    e_energy = mass * (c_speed_of_light**2)

    print("e = m * c^2 ...")
    print(f"m = mass = {mass}kg")
    print(f"C = Speed of Light = {c_speed_of_light}m/s")
    print(f"E = Energy = {e_energy} joules of energy")

if __name__=="__main__":
    main()
