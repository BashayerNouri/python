
# Foundations 3: Python
# Task Five

 # This is a system to assist a cashier, where the cashier has to enter the items bought,
 #               and at the end a receipt will be printed.

 # Edited: the total calculation


items = []


while True:
	name = input("item (enter \"done\" when finished): ")
	if(name != "done"):
		price = float(input("price: "))
		quantity = int(input("quantity: "))
		total_price = price * quantity
		items.append({"name": name, "price": total_price, "quantity" : quantity})


	else:
		print("-------------------")
		print("receipt")
		print("-------------------")

		total = 0
		for item in items:

			print (item["quantity"],item["name"], str('{:0.3f}'.format(item["price"])) + "KD")	
			total += item["price"]

		print("-------------------")
		print("total:", str('{:0.3f}'.format(total))  + "KD")
		break

		