"""leapdays()"""
from calendar import leapdays, isleap
begin_year = 2010
end_year = 2021
print(f"Number of leap years: since {begin_year} until {end_year} without include {end_year} are {leapdays(begin_year, end_year)} ")
print()

# Note: you can confirm what exactly years are leap
count_leap_years = 0
for year in range(begin_year, end_year):
    if isleap(year) == True:
        print(f"year: {year} is a leap year")
        count_leap_years += 1
    else: 
        print(f"year: {year} is NOT a leap year")
print(count_leap_years)