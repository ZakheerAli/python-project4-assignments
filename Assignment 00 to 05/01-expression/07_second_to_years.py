# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

def main():
    year=int(input("Enter Numbers of years: "))
    year_to_days = 365
    day_to_hours = 24 
    hour_to_minutes = 60
    minute_to_second = 60

    total_days_in_a_year = year * year_to_days
    total_hours_in_a_year = total_days_in_a_year * day_to_hours
    total_minutes_in_a_year =total_hours_in_a_year * hour_to_minutes
    total_seconds_in_a_year = total_minutes_in_a_year * minute_to_second

    print(f"There are {total_days_in_a_year} days in {year} years")
    print(f"There are {total_hours_in_a_year} hours in {year} years")
    print(f"There are {total_minutes_in_a_year} minutes in {year} years")
    print(f"There are {total_seconds_in_a_year} seconds in {year} years")

if __name__=="__main__":
    main()
    