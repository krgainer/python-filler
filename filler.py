import random
import time

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
	while gameboard_array[0][-1] == gameboard_array[-1][0]:
		print("duplicate, swapping @ ",gameboard_array[0][-1],gameboard_array[-1][0])
		gameboard_array[-1][0] = random.randrange(0, color_set)
	# return board and player colors
	return gameboard_array

def helpful_print(value:list):
	for i in value:
		print(i)

def available_colors(players, color_set):
	curr_color = [players[0]["current_color"], players[1]["current_color"]]
	prev_color = [players[0]["previous_color"], players[1]["previous_color"]]
	color_list = range(color_set)
	available_color_set = []
	for elm in color_list:
		if elm not in (curr_color + prev_color):
			available_color_set.append(elm)
	return available_color_set

def swap_colors(player, players, target_color):
	players[player]["previous_color"] = players[player]["current_color"]
	players[player]["current_color"] = target_color

def check_win_condition(players, square):
	total_cells = square * square
	if players[0]["score"] > total_cells // 2:
		return 0  # Player 0 wins
	elif players[1]["score"] > total_cells // 2:
		return 1  # Player 1 wins
	return None  # No winner yet

def game():
	pass

def traverse(player, players, color_set, gameboard):
	# this may or may not be the acutally recursive traversal function. 
	# it must spread the new color across current territory, capture adjacent cells, and count teritory. 
	# I'm tempted to create two "mask" arrays for each player, but that would get memory intesive kinda quickly? I mean each val in the array can be bool, but theres two of them.
	if player == 0:
		flood_fill(0,-1,color_set+1,gameboard,player)
	else:
		flood_fill(-1,0,color_set+1,gameboard,player)

def flood_fill(row, col, old_color, new_color, gameboard, color_set):
	# stop condition - out of bounds
	if row < 0 or row >= len(gameboard) or col < 0 or col >= len(gameboard[0]):
		return 0
	
	# stop condition - already visited (marked with color_set)
	if gameboard[row][col] == color_set:
		return 0
	
	# Stop condition - not player's territory and not capturable
	if gameboard[row][col] != old_color and gameboard[row][col] != new_color:
		return 0
	
	# Recursive step - this cell is either player's territory or capturable
	gameboard[row][col] = color_set  # Mark as visited
	count = 1
	
	# Recurse in 4 directions
	count += flood_fill(row + 1, col, old_color, new_color, gameboard, color_set)
	count += flood_fill(row - 1, col, old_color, new_color, gameboard, color_set)
	count += flood_fill(row, col + 1, old_color, new_color, gameboard, color_set)
	count += flood_fill(row, col - 1, old_color, new_color, gameboard, color_set)
	
	return count

def main():
	color_set = 7
	square = 6
	gameboard = []
	current_player = 0
	# this set is player 1, then player 2
	players = [
		{"current_color": None, "previous_color": None, "score": 1, "start_pos": (0, -1)},
		{"current_color": None, "previous_color": None, "score": 1, "start_pos": (-1, 0)}
	]
	gameboard = generate_inital_board(gameboard, square, color_set)
	
	# Initialize player colors from their starting positions
	players[0]["current_color"] = gameboard[0][-1]
	players[1]["current_color"] = gameboard[-1][0]
	
	print(f"Player One Number: {players[0]['current_color']} \nPlayer Two Number: {players[1]['current_color']}")
	
	while check_win_condition(players, square) == None:
		print("-"*200)
		print(f"Player One Current Score: {players[0]['score']}\nPlayer Two Current Score: {players[1]['score']}")
		helpful_print(gameboard)
		
		if current_player == 0:
			print(f"Player 1 - You can chose from any of these numbers: {available_colors(players, color_set)}")
		else:
			print(f"Player 2 - You can chose from any of these numbers: {available_colors(players, color_set)}")
		
		# TODO: Get player input for color choice
		# chosen_color = int(input("Choose a color: "))
		
		# TODO: Validate choice is in available_colors
		
		# TODO: Update player color and traverse
		# swap_colors(current_player, players, chosen_color)
		# traverse(current_player, players, color_set, gameboard)
		
		# Switch players
		current_player = 1 - current_player
		
		time.sleep(10)

main()