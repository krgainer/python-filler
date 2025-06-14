# Game Rules

## Setup:

	{square}x{square} grid with cells containing colors (numbers 0-{color_set-1})
	Player 1 starts in bottom-right corner
	Player 2 starts in top-left corner
	Starting corners cannot have adjacent cells of the same color as the corner (prevents instant expansion)

## Gameplay:

	Player 1 goes first
	On each turn, a player chooses a new color from available colors

	Available colors = all colors except:
		Their current color
		Their opponent's current color
		The color they used last turn (prevents camping)



## Territory Expansion:

### When a player chooses a color:

- All cells in their territory change to the new color
- Any cells adjacent (4-directional) to their territory that match the chosen color are captured
- This continues recursively (flood-fill) until no more adjacent matching cells exist



## Winning:

First player to control more than half the board (>{(square*square)//2} cells) wins

## Scoring:

Score = number of cells controlled by each player