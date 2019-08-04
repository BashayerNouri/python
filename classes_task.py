
# Foundations 3: Python
# Task Six


# HR system for a company. This company has two types of employees, normal employees and managers.

# Cases:
# 1) Actions should be from 1 to 5, any other numbers will print out (wrong action).
# 2) if lists are empty, it will print out (lists are empty).


from datetime import datetime

class Employee:

	date = datetime.now()
	today_year = date.year

	def __init__(self,name,age,salary,employment_date):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date
	
	def get_working_years(self):
		return (self.today_year - self.employment_date)


class Manager(Employee):

	def __init__(self,name,age,salary,employment_date,bonus_percentage):
		Employee.__init__(self,name,age,salary,employment_date)
		self.bonus_percentage = bonus_percentage

	def get_bonus(self):
		return (self.bonus_percentage * self.salary)


employees = []
managers = []


print ("    Welcome to HR Pro 2019")


while True:

	print ("    Choose an action to do:")
	print ("        1. show employees")
	print ("        2. show managers")
	print ("        3. add an employee")
	print ("        4. add a manager")
	print ("        5. exit \n ")

	action = int(input("what would you like to do? "))

	

	if (action == 1):

		if len(employees) == 0:
			
			print("-----------------")
			print("The list is empty, please add an employee to show results!")
			print("----------------- \n")

		else:
			for e_list in employees:
				
				print("-----------------")
				print("Employees")
				print("name: " + e_list.name + ", " + "age: " + str(e_list.age) + ", " + "salary: " + str(e_list.salary) + ", " 
					+ "working years: " + str(e_list.get_working_years()) + "\n" )
				print("----------------- \n")

	elif (action == 2):

		if len(managers) == 0:
			
			print("-----------------")
			print("The list is empty, please add an manager to show results!")
			print("----------------- \n")

		else:
			for m_list in managers:
				
				print("-----------------")
				print("Managers")
				print("name: " + m_list.name + ", " + "age: " + str(m_list.age) + ", " + "salary: " + str(m_list.salary) + ", " 
					+ "working years: " + str(m_list.get_working_years()) + ", " + "bonus: " + str(m_list.get_bonus()) + "\n" )
				print("----------------- \n")

	elif (action == 3):

		ename = input("name: ")
		eage = int(input("age: "))
		esalary = int(input("salary: "))
		eyear = int(input("employement year: "))
		employee = Employee(ename,eage,esalary,eyear)
		employees.append(employee)

		
		print("-----------------")
		print ("Employee added succesfully \n")

	elif (action == 4):

		mname = input("name: ")
		mage = int(input("age: "))
		msalary = int(input("salary: "))
		myear = int(input("employement year: "))
		mbonus = float(input("bonus percentage: "))
		manger = Manager(mname,mage,msalary,myear,mbonus)
		managers.append(manger)

		print("-----------------")
		print ("Employee added succesfully \n")

	

	elif (action == 5):
		break

	
	else:
		print("Action not available! .. please select from 1 to 5.")
		print("----------------- \n")
