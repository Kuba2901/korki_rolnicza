from car_rental import Car, CarRental


def main():
	print("CAR RENTAL\n")
	file_name = input("File name > ")
	rental = CarRental(file_name)
	
	running = True
	while running:
		print("""
Choose option
1. Add new car
2. Remove car
3. View car
4. Rent car
5. Quit
		""")

		option = input("> ")
		if "1" is option:
			print("")
			car_data = input("[id] [year] [brand] [color]: ")
			car_values = car_data.split(" ")
			rental.add_car(car_values[0], car_values[1], car_values[2], car_values[3])
			print("[+] Car added")

		if "2" is option:
			print("")
			id = input("[id]: ")
			if rental.delete_car(id):
				print("[X] Car removed")
			else:
				print("[!] No car removed")
		
		if "3" is option:
			print("")
			id = input("[id]: ")
			rental.view_car(id)

		if "4" is option:
			print("")
			id = input("[id]: ")
			available = rental.toggleAvailability(id)

			if available is None:
				print("[!] No car with this ID")
			elif available is True:
				print("[ok] The car is back")
			else:
				print("[ok] The car was rented")

		if "5" is option:
			running = False

main()