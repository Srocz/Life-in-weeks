#Calulates how many months, weeks and days a person has left to live based on their current age if
# they were to live up to 90 years old.

age = input("What is your current age?")

age_int = int(age)

life_span = 90

remaining_years = (life_span - age_int)

days_in_year = 365
weeks_in_year = 52
months_in_year = 12

days_left = (remaining_years * days_in_year)
weeks_left = (remaining_years * weeks_in_year)
months_left = (remaining_years * months_in_year)

print(f"you have {days_left} days, {weeks_left} weeks, {months_left} months left.")

