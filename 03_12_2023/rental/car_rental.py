from typing import Dict, List
import json

class Car:
	# Constructor with optional parameters
	def __init__(self, id = 1, year = 2000, brand = "brand", color = "color") -> None:
		self.id = id
		self.year = year
		self.brand = brand
		self.color = color
		self.available = True

	# returns the instance's data in the json format
	def toJson(self) -> Dict:
		return {
			"id": self.id,
			"year": self.year,
			"brand": self.brand,
			"color": self.color	,
			"available": self.available
		}

	# Updates the instance's data with the data read from a json object
	def fromJson(self, data) -> None:
		self.id = data['id']
		self.year = data["year"]
		self.brand = data["brand"]
		self.color = data["color"]
		self.available = data["available"]

class CarRental:
	def __init__(self, file_name: str) -> None:
		self.file_name = file_name
		self.cars = self.get_cars()

	# Gets the cars from the .json file and uploads them to the instances' list
	def get_cars(self) -> List[Car]:
		# 1. Try to open the file
		try:
			# 1a. The file was opened successfully
			file = open(self.file_name, "r")
		except:
			# 1b. An error occured - the file doesn't exist
			with open(self.file_name, "w") as file:
				# Put an empty dictionary in the file
				json.dump({}, file)
			# Reopen the file
			file = open(self.file_name, "r")

		# 2. We load the values into a dictionary
		data = json.load(file) 

		# 3. Create an empty list
		cars_list = []

		# 4. Iterate over the values in the dictionary
		for v in data.values():
			car = Car()
			car.fromJson(v)

			# Append the car to the list
			cars_list.append(car)

		file.close()
		return (cars_list)

	# Adds a new car to the listing
	def add_car(self, id: int, year: int, brand: str, color: str) -> None:
		new_car = Car(id, year, brand, color)
		self.cars.append(new_car)
		self.dump_to_file()

	# Updates the .json file
	def dump_to_file(self) -> None:
		data = {}
		for car in self.cars:
			car_id = str(car.id)
			car_json = car.toJson()
			data[car_id] = car_json

		with open(self.file_name, "w") as file:
			json.dump(data, file, indent=2)
	
	# Deletes the car from the rental listings
	def delete_car(self, id: int) -> bool:
		for car in self.cars:
			if car.id == id:
				self.cars.remove(car)
				self.dump_to_file()
				return True
		return False

	# Toggles the car state (available / not available)
	def toggleAvailability(self, id: int) -> bool:
		for car in self.cars:
			if car.id == id:
				car.available = not car.available
				self.dump_to_file()
				return car.available
		return None

	# Displays the post in the JSON format
	def view_car(self, id: int) -> None:
		for car in self.cars:
			if car.id == id:
				print(car.toJson())
				break