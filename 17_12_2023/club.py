from typing import Dict, List, Optional
import json

class Player:
	# The player constructor
	# Args: id: Optional[int], first_name: Optional[str], last_name: Optional[str], date_of_birth: Optional[str], first_team_player: Optional[bool]
	# Returns: None
	def __init__(self, id: Optional[int] = 1, first_name: Optional[str] = "first_name", last_name: Optional[str] = "last_name", date_of_birth: Optional[str] ="date_of_birth", first_team_player: Optional[bool] = True) -> None:
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.date_of_birth = date_of_birth
		self.first_team_player = first_team_player

	# Method to convert the Club class instance to a JSON format
	# Args: None
	# Returns: Dict
	def to_json(self) -> Dict:
		return {
			"id": self.id,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"date_of_birth": self.date_of_birth,
			"first_team_player": self.first_team_player
		}

	# Method to update the instance's data with data from a JSON file
	# Args: data: Dict
	# Returns: None
	def from_json(self, data: Dict) -> None:
		self.id = int(data["id"])
		self.first_name = data["first_name"]
		self.last_name = data["last_name"]
		self.date_of_birth = data["date_of_birth"]
		self.first_team_player = bool(data["first_team_player"])


	# Overriden comparison operator
	# Args: other: Club
	# Returns: bool
	def __eq__(self, other) -> bool:
		if self.first_name == other.first_name and self.last_name == other.last_name and self.date_of_birth == other.date_of_birth and self.first_team_player == other.first_team_player:
			return (True)
		else:
			return (False)


class Club:
	# The Club constructor
	# Args: file_name: str
	# Returns: None
	def __init__(self, file_name: str) -> None:
		self.file_name = file_name
		self.players = self.get_players()
		self.captain_id = None

	# The method to get the Players from the given file in JSON format and return a List of Playerss class instances
	# Args: None
	# Returns: List[Club]
	def get_players(self) -> List[Player]:
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
		players_list = []

		# 3b. (new) get the players data
		# players_data = data.get("players")

		# 3c. (new) get the team_captain id
		# captain_data = data.get("captain_id")
		
		# if captain_data is not None:
		# 	self.captain_id = int(captain_data)
		
		for v in data.values():
			player = Player()
			player.from_json(v)

			# Append the car to the list
			players_list.append(player)

		file.close()
		return (players_list)

	# The method to add a new player to the file
	# Args: id: int, first_name: str, last_name: str, date_of_birth: str, first_team_player: bool
	# Returns: bool
	def add_player(self, id: int, first_name: str, last_name: str, date_of_birth: str, first_team_player: bool) -> bool:
		new_player = Player(int(id), first_name, last_name, date_of_birth, bool(first_team_player))
		self.players.append(new_player)
		self.dump_to_file()
		return (True)

	# The method to update the file
	# Args: None
	# Returns: None
	def dump_to_file(self) -> None:
		data = {}

		for player in self.players:
			player_id = str(player.id)
			player_json = player.to_json()
			data[player_id] = player_json

		with open(self.file_name, "w") as file:
			json.dump(data, file, indent=2)
	
	# The method to remove a player from the file and the list
	# Args: id: int
	# Returns: bool
	def delete_player(self, id: int) -> bool:
		id = int(id)
		for player in self.players:
			if player.id == id:
				self.players.remove(player)
				self.dump_to_file()
				return (True)
		return (False)

	# The method to change the team captain
	# Args: id: int
	# Returns: bool
	def captain_uncaptain_player(self, id: int) -> bool:
		id = int(id)
		for player in self.players:
			# The player of the given ID exists
			if player.id == id:
				self.captain_id = player.id
				self.dump_to_file()
				return (True)
		return (False)

	# The method to promote / demote a player from the first_team
	# Args: id: int
	# Returns: bool
	def promote_demote_player(self, id: int) -> bool:
		id = int(id)
		for player in self.players:
			if player.id == id:
				player.first_team_player = not player.first_team_player
				if player.first_team_player:
					self.dump_to_file()
					return (True)
				else:
					return (False)
		return (None)

	# The method to view the details of the player with a given id
	# Args: id: int
	# Returns: None
	def view_player(self, id: int) -> Dict:
		id = int(id)
		for player in self.players:
			if player.id == id:
				return (player.to_json())
		return (None)

	def print_123(self) -> str:
		ret = ""
		for i in range(3):
			ret += f"{i + 1}\n"
		return (ret)

	def print_hello(self) -> str:
		return "hello" + f" {self.print_123()}"

	