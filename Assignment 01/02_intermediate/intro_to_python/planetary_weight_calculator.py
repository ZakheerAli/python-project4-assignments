# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.
# Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

# Mercury: 37.6%

# Venus: 88.9%

# Mars: 37.8%

# Jupiter: 236.0%

# Saturn: 108.1%

# Uranus: 81.5%

# Neptune: 114.0%

# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.

# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets.


# """ WAY 1 """

# def main():
#     print("🚀 Welcome to the Interplanetary Weight Calculator!")
#     print("Find out what your weight would be on other planets in our solar system. 🌍✨")
#     gravity_ratio_of_all_planet={
#         "mercury":37.6 /100,
#         "venus": 88.9/100,
#         "mars":37.8/100,
#         "jupiter":236.0/100,
#         "saturn": 108.1/100,
#         "uranus": 81.5/100,
#         "neptune": 114.0/100
#     }
#     earth_weight:int=float(input("Enter Your Weight on Earth: "))
#     print("In which planet you want to find your weight:\n1:Mercury\n2:Venus\n3:Mars\n4:Jupiter\n5:Saturn\n6:Uranus\n7:Neptune")
#     planet:str=input("Enter planet from the above list: ")
#     planet = planet.strip().lower()
#     if planet == "mercury":
#         weight_on_mercury= earth_weight * gravity_ratio_of_all_planet["mercury"]
#         print(f"Your weight on Mercury is {round(weight_on_mercury,2)}")
#     elif planet == "venus":
#          weight_on_venus= earth_weight * gravity_ratio_of_all_planet["venus"]
#          print(f"Your weight on venus is {round(weight_on_venus,2)}")
#     elif planet == "mars":
#          weight_on_mars= earth_weight * gravity_ratio_of_all_planet["mars"]
#          print(f"Your weight on mars is {round(weight_on_mars,2)}")
#     elif planet == "jupiter":
#          weight_on_jupiter= earth_weight * gravity_ratio_of_all_planet["jupiter"]
#          print(f"Your weight on jupiter is {round(weight_on_jupiter,2)}")
#     elif planet == "saturn":
#          weight_on_saturn= earth_weight * gravity_ratio_of_all_planet["saturn"]
#          print(f"Your weight on saturn is {round(weight_on_saturn,2)}")
#     elif planet == "uranus":
#          weight_on_uranus= earth_weight * gravity_ratio_of_all_planet["uranus"]
#          print(f"Your weight on uranus is {round(weight_on_uranus,2)}")
#     elif planet == "neptune":
#          weight_on_neptune= earth_weight * gravity_ratio_of_all_planet["neptune"]
#          print(f"Your weight on neptune is {round(weight_on_neptune,2)}")
#     else:
#          print("Inavlid Input :")

    

# if __name__=="__main__":
#     main()



# """ WAY 2 """
def main():
    print("🌌 WELCOME TO THE PLANETARY WEIGHT CALCULATOR 🌍✨") 

    gravity_ratio_of_all_planets = {
        "mercury": 37.6 / 100,
        "venus": 88.9 / 100,
        "mars": 37.8 / 100,
        "jupiter": 236.0 / 100,
        "saturn": 108.1 / 100,
        "uranus": 81.5 / 100,
        "neptune": 114.0 / 100
    }

    try:
        weight_on_earth = float(input("Enter your weight on Earth (in kg): "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return

    print("\n🌠 Choose a planet from this list:")
    capitalized_planets = []
    for planet in gravity_ratio_of_all_planets:
        capitalized_planets.append(planet.capitalize())
    print(", ".join(capitalized_planets))   

    planet = input("Enter planet: ").strip().lower()

    if planet in gravity_ratio_of_all_planets:
        weight_on_planet = weight_on_earth * gravity_ratio_of_all_planets[planet]
        print(f"✅ Your weight on {planet.capitalize()} is {round(weight_on_planet, 2)} kg.")
    else:
        print("❌ Invalid input. Please enter a valid planet from the list.") 

if __name__ == "__main__":
    main()
