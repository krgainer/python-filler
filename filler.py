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
		print("duplicate, swapping @ ",player_one_currenet_color,player_two_currenet_color)
		gameboard_array[-1][0] = random.randrange(0, color_set)
		player_two_currenet_color = gameboard_array[-1][0]
	# return board and player colors
	return gameboard_array

def helpful_print(value:list):
	for i in value:
		print(i)

def player_current_color(player,gameboard):
	if player == 0:
		return gameboard[0][-1]
	else:
		return gameboard[-1][0]

def available_colors(gameboard, prev_color,color_set):
	curr_color = [player_current_color(0,gameboard),player_current_color(1,gameboard)]
	color_list = range(color_set)
	available_color_set = []
	for elm in color_list:
		if elm not in (curr_color + prev_color):
			available_color_set.append(elm)
	return available_color_set

def swap_colors(player, player_previous_colors, player_current_colors, target_color):
	player_previous_colors[player] = player_current_colors[player]
	player_current_colors[player] = target_color
	return player_previous_colors, player_current_colors

def check_win_condition():
	pass

def game():
	pass

def traverse(player, player_current_colors, color_set, gameboard):
	# this may or may not be the acutally recursive traversal function. 
	# it must spread the new color across current territory, capture adjacent cells, and count teritory. 
	# I'm tempted to create two "mask" arrays for each player, but that would get memory intesive kinda quickly? I mean each val in the array can be bool, but theres two of them.
	if player == 0:
		flood_fill(0,-1,color_set+1,gameboard,player)
	else:
		flood_fill(-1,0,color_set+1,gameboard,player)


def flood_fill(row, col, new_color, gameboard, player):
	pass



def main():
	color_set = 7
	square = 6
	gameboard = []
	current_player = 0
	# this set is player 1, then player 2
	player_scores = [1,1]
	player_previous_colors = [None, None]
	gameboard = generate_inital_board(gameboard,square, color_set)
	print(f"Player One Number: {player_current_color(0,gameboard)} \nPlayer Two Number: {player_current_color(1,gameboard)}")
	while (check_win_condition()) == None:
		print("-"*200)
		print(f"Player One Current Score: {player_scores[0]}\nPlayer Two Current Score: {player_scores[1]}")
		helpful_print(gameboard)
		if current_player == 0:
			print(f"Player 1 - You can chose from any of these numbers: {available_colors(gameboard,player_previous_colors,color_set)}")
			time.sleep(10)
			

main()