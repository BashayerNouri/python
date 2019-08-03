
# Foundations 3: Python
# Task Three

# This is an age calculator where the user will input his birth date and 
#             the program will give him back his age.


from datetime import date

today = date.today()

def check_birthdate(year,month,day):
  if(year >= today.year and month >= today.month and day > today.day):
    print("This birthdate is from the future! Try another.")
  else:
    return calculate_age(year,month,day)


def calculate_age(year,month,day):
	if (month <= 12) and (day <= 31):
		day = abs(today.day - day)
		month = abs(today.month - month) 
		year = abs(today.year - year)
		print("You are " + str(year) +" years, " + str(month) + " months, and " + str(day) + " days")
	else:
		print("This birthdate is invalid! Try another.")



year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))

check_birthdate(year,month,day)
