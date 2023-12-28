from club import Player, Club
import unittest
from mock import patch, mock
import os

import json

class TestPlayer(unittest.TestCase):
	def test_to_json(self):
		player = Player(1, "jakub", "nenczak", "29.01.2003", True)
		expected = {
			"id": 1,
			"first_name": "jakub",
			"last_name": 'nenczak',
			"date_of_birth": "29.01.2003",
			"first_team_player": True
		}

		self.assertEqual(player.to_json(), expected)

	def test_from_json(self):
		player_expected = Player(1, "jakub", "nenczak", "29.01.2003", True)
		data = {
			"id": 1,
			"first_name": "jakub",
			"last_name": 'nenczak',
			"date_of_birth": "29.01.2003",
			"first_team_player": True
		}
		player = Player()
		player.from_json(data)
		
		self.assertEqual(player.first_name, player_expected.first_name)
		self.assertEqual(player.last_name, player_expected.last_name)
		self.assertEqual(player.date_of_birth, player_expected.date_of_birth)
		self.assertEqual(player.first_team_player, player_expected.first_team_player)
		self.assertEqual(player, player_expected)

class TestClub(unittest.TestCase):
	def tearDown(self):
		try:
			os.remove("test_file.json")
		except:
			pass

	# def test_view_player(self):
	# 		with patch.object(Club, 'get_players', return_value=[Player(1, "jakub", "nenczak", "29.01.2003", True)]):
	# 			expected = {
	# 				"id": 1,
	# 				"first_name": "jakub",
	# 				"last_name": 'nenczak',
	# 				"date_of_birth": "29.01.2003",
	# 				"first_team_player": True
	# 			}

	# 			club_instance = Club("test_file.json")
	# 			players = club_instance.players
	# 			ret = club_instance.view_player(1)
	# 			self.assertEqual(ret, expected)


	@patch("club.Club.get_players")
	def test_view_player(self, mocked_get_player):
		mocked_get_player.return_value = [Player(1, "marcelina", "gorka", "29.08.2007", True)]
		expected = {
			"id": 1,
			"first_name": "marcelina",
			"last_name": "gorka",
			"date_of_birth": "29.08.2007",
			"first_team_player": True
		} 
		club_instance = Club("test_file.json")
		players = club_instance.players
		ret = club_instance.view_player(1)
		self.assertEqual(ret, expected)

	@patch("club.Club.get_players")
	def test_view_player_none(self, mocked_get_players):
		club_instance = Club("test_file.json")
		mocked_get_players.return_value = []
		players = club_instance.players
		ret = club_instance.view_player(1)
		self.assertEqual(ret, None)

	
	def test_player_promoted(self):
		with patch.object(Club, 'get_players', return_value=[Player(1, "jakub", "nenczak", "29.01.2003", False)]):
				club_instance = Club("test_file.json")
				players = club_instance.players
				ret = club_instance.promote_demote_player(1)
				self.assertTrue(ret)

	def test_player_demoted(self):
		with patch.object(Club, 'get_players', return_value=[Player(1, "jakub", "nenczak", "29.01.2003", True)]):
				club_instance = Club("test_file.json")
				players = club_instance.players
				ret = club_instance.promote_demote_player(1)
				self.assertFalse(ret)

	def test_player_promoted_demoted_none(self):
		with patch.object(Club, 'get_players', return_value=[]):
				club_instance = Club("test_file.json")
				players = club_instance.players
				ret = club_instance.promote_demote_player(1)
				self.assertIsNone(ret)

	def test_captain_uncaptain_player_changed(self):
		with patch.object(Club, 'get_players', return_value=[Player(1, "jakub", "nenczak", "29.01.2003", True)]):
				club_instance = Club("test_file.json")
				players = club_instance.players
				captain = club_instance.captain_id = 1
				ret = club_instance.captain_uncaptain_player(1)
				self.assertTrue(ret)

	def test_captain_uncaptain_player_not_changed(self):
		with patch.object(Club, 'get_players', return_value=[Player(1, "jakub", "nenczak", "29.01.2003", True)]):
				club_instance = Club("test_file.json")
				players = club_instance.players
				ret = club_instance.captain_uncaptain_player(2)
				self.assertFalse(ret)

	def test_delete_player(self):
		club_instance = Club("test_file.json")
		club_instance.add_player(1, "jakub", "nenczak", "29.01.2003", True)
		self.assertEqual(len(club_instance.players), 1)
		club_instance.delete_player(1)
		self.assertEqual(len(club_instance.players), 0)


	def test_delete_player_failed(self):
		club_instance = Club("test_file.json")
		club_instance.add_player(1, "jakub", "nenczak", "29.01.2003", True)
		self.assertEqual(len(club_instance.players), 1)
		club_instance.delete_player(2)
		self.assertEqual(len(club_instance.players), 1)

	def test_add_player(self):
		club_instance = Club("test_file.json")
		club_instance.add_player(1, "jakub", "nenczak", "29.01.2003", True)
		self.assertEqual(len(club_instance.players), 1)
	
	def test_dump_to_file(self):
		file_name = "test_file.json"
		file_creating_instance = Club(file_name)

		with patch.object(Club, 'get_players', return_value=[Player(1, "jakub", "nenczak", "29.01.2003", True)]):
				club_instance = Club(file_name)
				players = club_instance.players
				with open(file_name, "r") as file:
					data = json.load(file)

				self.assertEqual(data, {})

				club_instance.dump_to_file()
				with open(file_name, "r") as file:
					data = json.load(file)

				expected = {
					"id": 1,
					"first_name": "jakub",
					"last_name": 'nenczak',
					"date_of_birth": "29.01.2003",
					"first_team_player": True
				}
				self.assertEqual(data["1"], expected)

	def test_get_players(self):
		file_name = "test_file.json"
		data = {
			"1": {
					"id": 1,
					"first_name": "jakub",
					"last_name": 'nenczak',
					"date_of_birth": "29.01.2003",
					"first_team_player": True
				}
		}

		player_expected = Player()
		player_expected.from_json(data["1"])

		with open(file_name, "w") as file:
			json.dump(data, file, indent=2)
		
		club_instance = Club(file_name)
		self.assertEqual(len(club_instance.players), 1)
		self.assertEqual(player_expected, club_instance.players[0])

if __name__ == '__main__':
	unittest.main()
