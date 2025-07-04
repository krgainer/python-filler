import random
import time
import sys

sys.setrecursionlimit(10000) # is this an issue? probably

debug_print = True

def generate_inital_board(gameboard_array, square, color_set):
	#generate gameboard
	for i in range(square):
		temp_list=[]
		for i in range(square):
			current_color = random.randrange(0, color_set)
			temp_list.append(current_color)
			del current_color
		gameboard_array.append(temp_list)
		del temp_list
	#genrerate player colors
	# this is jank and also doesnt account for starting colors touching nearby colors. players should never be able to start at anything besides 1 point (no touching like-colors)
	while gameboard_array[0][-1] == gameboard_array[-1][0]:
		if debug_print:
			print("duplicate, swapping @ ",gameboard_array[0][-1],gameboard_array[-1][0])
		gameboard_array[-1][0] = random.randrange(0, color_set)
	# return board and player colors
	return gameboard_array

def helpful_print(value:list):
	for i in value:
		print(i)

def available_colors(player, players, color_set):
	curr_color = [players[0]["current_color"], players[1]["current_color"]]
	prev_color = [players[player]["previous_color"]]
	color_list = range(color_set)
	available_color_set = []
	for elm in color_list:
		if elm not in (curr_color + prev_color):
			available_color_set.append(elm)
	return available_color_set

def swap_player_color(player, players, target_color):
	players[player]["previous_color"] = players[player]["current_color"]
	players[player]["current_color"] = target_color
	return players

def check_win_condition(players, square):
	total_cells = square * square
	if players[0]["score"] > total_cells // 2:
		return 0  # player 0 wins
	elif players[1]["score"] > total_cells // 2:
		return 1  # player 1 wins
	return None  # no winner yet

def get_player_color_input(current_player, players, color_set):
	chosen_color = None
	while(chosen_color == None):
		temp_chosen_color = input("Choose a color: ").strip().lower()
		try:
			temp_chosen_color = int(temp_chosen_color)
		except:
			print("Please enter a number!")
		if temp_chosen_color not in available_colors(current_player, players, color_set):
			print(f"Please enter one of the available colors: {available_colors(current_player, players, color_set)}")
		else:
			chosen_color = temp_chosen_color
	return chosen_color

def traverse(player, players, color_set, gameboard,square):
	# get starting position for the player
	start_row, start_col = players[player]["start_pos"]
	if start_row < 0:
		start_row = square-1 # get abs, not array rel
	if start_col < 0:
		start_col = square-1 # get abs, not array rel
	old_color = gameboard[start_row][start_col] # get the old color (what the player's territory currently is)
	new_color = players[player]["current_color"]
	temp_marker = color_set  # use color_set as the temp marker value (its +1 what can be in available_colors)
	
	# flood fill to mark territory
	count = flood_fill(start_row, start_col, old_color, new_color, gameboard, temp_marker)

	# convert all marked cells (temp_marker) to the actual new color
	for i in range(len(gameboard)):
		for j in range(len(gameboard[0])):
			if gameboard[i][j] == temp_marker:
				gameboard[i][j] = new_color
	
	# update player's score
	players[player]["score"] = count
	return count

def flood_fill(row, col, old_color, new_color, gameboard, temp_marker):
	# stop condition - out of bounds
	if row < 0 or row >= len(gameboard) or col < 0 or col >= len(gameboard[0]):
		if debug_print:
			print(f"stop @ row {row}, col {col}. oob")
		return 0
	
	# stop condition – already visited (marked with temp_marker)
	if gameboard[row][col] == temp_marker:
		if debug_print:
			print(f"stop @ row {row}, col {col}. marked")
		return 0
	
	# stop condition - not player's territory and not capturable
	if gameboard[row][col] != old_color and gameboard[row][col] != new_color:
		if debug_print:
			print(f"stop @ row {row}, col {col}. not valid take")
		return 0
	
	# recursive step - this cell is either player's territory or capturable
	gameboard[row][col] = temp_marker  # Mark as visited
	count = 1
	if debug_print:
		print(f"oh hi mark @ row {row}, col {col}")
	
	# recurse in 4 directions (should it be 8?)
	count += flood_fill(row + 1, col, old_color, new_color, gameboard, temp_marker)
	count += flood_fill(row - 1, col, old_color, new_color, gameboard, temp_marker)
	count += flood_fill(row, col + 1, old_color, new_color, gameboard, temp_marker)
	count += flood_fill(row, col - 1, old_color, new_color, gameboard, temp_marker)
	
	return count

def game(color_set, square):
	gameboard = []
	current_player = 0

	# this set is player 1, then player 2
	players = [
		{"current_color": None, "previous_color": None, "score": 1, "start_pos": (0, -1)},
		{"current_color": None, "previous_color": None, "score": 1, "start_pos": (-1, 0)}
	]

	gameboard = generate_inital_board(gameboard, square, color_set)
	
	# initialize player colors from their starting positions
	players[0]["current_color"] = gameboard[0][-1]
	players[1]["current_color"] = gameboard[-1][0]
	
	print(f"Player One Number: {players[0]['current_color']} \nPlayer Two Number: {players[1]['current_color']}")
	
	while check_win_condition(players, square) == None:
		print("-"*200)
		print(f"Player One Current Score: {players[0]['score']}\nPlayer Two Current Score: {players[1]['score']}")
		helpful_print(gameboard)
		
		if current_player == 0:
			print(f"Player 1 - You can chose from any of these numbers: {available_colors(current_player, players, color_set)}")
		else:
			print(f"Player 2 - You can chose from any of these numbers: {available_colors(current_player, players, color_set)}")
		
		chosen_color = get_player_color_input(current_player, players, color_set)

		players = swap_player_color(current_player, players, chosen_color)
		traverse(current_player, players, color_set, gameboard,square)
		
		# switch players
		current_player = 1 - current_player

	print("!"*500)
	print("Final board:")
	current_player = 1 - current_player # switch back to the winner
	helpful_print(gameboard)
	print(f"Player One Final Score: {players[0]['score']}\nPlayer Two Final Score: {players[1]['score']}")
	print (f"Player {current_player+1} Wins!")


def main():
	color_set = 6
	square = 128
	game(color_set,square)
	
main()