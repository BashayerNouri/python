
# Foundations 3: Python
# Task Four

# A recruitment system. This code ask the user a few questions and depending on his answers the 
#                      system will either accept or decline the applicant.


# Acceptance will only be for entry level or fresh grad with these requirements:
# 1) Age should be more than 22 and less than 30.
# 2) Experience years has to be from 0-5 (entry level).
# 3) Python and PHP has to be his skills.



skills = ["swimming", "make music", "video maker", "php", "python", "acting"]
cv = {}

cv["name"] = input("name: ")
cv["age"] = int(input("age: "))
cv["experience"] = int(input("how many years of experience do you have? "))
cv["skills"] = []


# enumerate() - returns an Enumerate Object
for i, skill in enumerate(skills,1):
  print(i, '- ' + skill, sep='')

s1 = int(input("choose a skill from above: "))
s2 = int(input("choose another skill from above: "))


cv["skills"].append(s1)
cv["skills"].append(s2)


# In case the user has PHP and Python as his skills
if (s1 == 4 or s1 == 5 and s2 == 4 or s2 == 5):
	# In case the age is equal or between 22 and 30
	if (cv["age"] >= 22 and cv["age"] <= 30):
		# In case the experience is equal or between 0 and 5
		if(cv["experience"] >= 0 and cv["experience"] <= 5):
			print("you have been accepted, " + cv["name"].title())
		else:
			print("Sorry " + cv["name"].title() + ", we are looking for entry level")
	else:
		print("Sorry " + cv["name"].title() + ", we are looking for certain ages")

else:
	print("Sorry " + cv["name"].title() + ", better luck next time.")

