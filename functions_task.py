
# Foundations 3: Python
# Task Three

# This is an age calculator where the user will input his birth date and 
#             the program will give him back his age.


# Tested: 21-12-1994 = You are 24 years, 7 months, and 13 days
# Tested: 21-12-3000 = This birthdate is from the future! Please try another.



from datetime import datetime

today = datetime.now()


def check_birthdate(year,month,day):

	birthdate = datetime(year,month,day)

	if(birthdate > today):
		return False
	else:
		return True
    


def calculate_age(year,month,day):

	birthdate = datetime(year,month,day)

	month_in_days = 30.4167 # one month = 30.4167 days
	year_in_days = 365.2422 # ref: https://www.grc.nasa.gov/WWW/k-12/Numbers/Math/Mathematical_Thinking/calendar_calculations.htm

	age = today - birthdate
	age_in_days = age.days
	age_in_years = int(age_in_days / year_in_days)
	age_in_days = age_in_days % year_in_days
	age_in_month = int(age_in_days / month_in_days)
	age_in_days = round(age_in_days % month_in_days)

	print("You are " + str(age_in_years) +" years, " + str(age_in_month) + " months, and " + str(age_in_days) + " days")


year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))

if check_birthdate(year,month,day):
	calculate_age(year,month,day)
else:
	print("This birthdate is from the future! Please try another.")