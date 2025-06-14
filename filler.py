import random

def generate_inital_board(gameboard_array):
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
	player_one_currenet_color = gameboard[0][-1]
	player_two_currenet_color = gameboard[-1][0]
	while player_one_currenet_color == player_two_currenet_color:
		print("duplicate, swapping @ ",player_one_currenet_color,player_two_currenet_color)
		gameboard[-1][0] = random.randrange(0, color_set)
		player_two_currenet_color = gameboard[-1][0]
	# return board and player colors
	return gameboard_array, [player_one_currenet_color, player_two_currenet_color]

def helpful_print(value:list):
	for i in value:
		print(i)

def available_colors(curr_color, prev_color):
	color_list = range(color_set)
	available_color_set = []
	for elm in color_list:
		if elm not in (curr_color + prev_color):
			available_color_set.append(elm)
	return available_color_set

def swap_colors(player,target_color):
	pass

def check_win_condition():
	pass

def game():
	pass

def main():
	global gameboard, color_set, square
	color_set = 7
	square = 6
	gameboard = []
	current_player = 0
	# this set is player 1, then player 2
	player_scores = [1,1]
	player_previous_colors = [None, None]
	player_current_colors = [None, None]
	gameboard, player_current_colors = generate_inital_board(gameboard)
	print(f"Player One Number: {player_current_colors[0]} \nPlayer Two Number: {player_current_colors[1]}")
	while (check_win_condition()) == None:
		print("-"*200)
		helpful_print(gameboard)
		if current_player == 1:
			print(f"Player 1 - You can chose from any of these numbers: {available_colors(player_current_colors,player_previous_colors)}")
			

main()