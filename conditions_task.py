
# Foundations 3: Python
# Task Two


# This is a calculator. the code ask the user for two numbers and the mathematical operation 
#                             and then print the result of that operation.





first = input("Enter the first number: ")
second = input("Enter the second number: ")
operation = input("Choose the operation (+, -, /, *): ")


if (first.isdigit()) and (second.isdigit()):
  if operation == "+":
  	result = int(first) + int(second)
  	print("The answer is " + str(result))  	     

  elif operation == "-":
  	result = int(first) - int(second)
  	print("The answer is " + str(result))

  elif operation == "*":
  	result = int(first) * int(second)
  	print("The answer is " + str(result))

  elif operation == "/":
  	result = int(first) / int(second)
  	print("The answer is " + str(result))
  
  else:
# If the user added an alphabet in the operation area
  	print("The operation is not valid!, The operation was not any of the choices(+, -, *, /)")

else:
# 	         Cases: 
# If the user added an alphabet in:
# 1) one of the inputs
# 2) two of the inputs
# 3) one of the inputs and in the operation
# 4) all of them.
    print("Not valid, check the inputs or the operation")