
# Foundations 3: Python
# Task Five

 # This is a system to assist a cashier, where the cashier has to enter the items bought,
 #               and at the end a receipt will be printed.


cashier = {'items' : []}


while True:
	name = input("item (enter \"done\" when finished): ")
	if(name != "done"):
		price = float(input("price: "))
		quantity = int(input("quantity: "))
		total = price * quantity
		cashier["items"].append({"name": name, "price": price, "quantity" : quantity, "total" : total})


	else:
		print("-------------------")
		print("receipt")
		print("-------------------")
		for values in cashier["items"]:

			print(values["quantity"], values["name"],'{:{width}.{prec}f}'.format(values["total"], width=5, prec=3),"KD")

		print("-------------------")

		# wrong calculation output if more than one item
		print("total:",'{:{width}.{prec}f}'.format(sum(values['total'] for item in cashier['items']), width=5, prec=3), "KD") 
		break
	

