from club import Club, Player


def main():
	print("VOLLEYBALL CLUB\n")
	file_name = input("File name > ")
	club = Club(file_name)
	
	running = True
	while running:
		print("""
Choose option
1. Add new player
2. Remove player
3. View player
4. Promote / demote player
5. Make player the captain
6. Quit
		""")

		option = input("> ")
		if "1" == option:
			print("New player")
			player_data = input("[id: int], [first_name: str], [last_name: str], [date_of_birth: str], [first_team_player: bool]: ")
			player_values = player_data.split(" ")
			club.add_player(player_values[0], player_values[1], player_values[2], player_values[3], player_values[4])

		if "2" == option:
			print("Deleting Player")
			id = input("[id]: ")
			if club.delete_player(id):
				print("Player removed")
			else:
				print("No player removed")
		
		if "3" == option:
			print("Viewing player details")
			id = input("[id]: ")
			print(club.view_player(id))

		if "4" == option:
			print("Promoting / demoting player")
			id = input("[id]: ")
			promoted = club.promote_demote_player(id)
			print("The player has been", "demoted" if not promoted else "promoted")

		if "5" == option:
			print("Chaning captain")
			id = input("[id]: ")
			changed = club.captain_uncaptain_player(id)
			print("The captain has", "not" if not changed else "", "been changed")

		if "6" == option:
			running = False

main()