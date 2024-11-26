def check_leap_years(start_year):
    # Function to check if a year is a leap year
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
    
    # Iterate from the start year to 2025
    for year in range(start_year, 2026):
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

# Get the start year from the user
start_year = int(input("Enter the start year: "))

# Call the function
check_leap_years(start_year)
