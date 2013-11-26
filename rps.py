#Rock, Paper, Scissors:
"""Write a program to simulate the paper-rock-scissor game. Each of the two players type in P, R, or S. The program then announces the winner based on the rule: Paper covers Rock, Rock breaks Scissors, Scissors cut Paper, or Nobody wins. Be sure to allow the players to use lowercase as well as uppercase letters."""
"""You MUST implement a function that takes the choices that both the players made and returns 1 if the player 1 won and 2 if the player 2 won and 0 if it is a tie. So the logic of deciding who won based on the rock, paper, scissor rule must be programmed inside this function."""
"""You MUST call this function to decide who won and you must display the result of the game based on the return value of the function."""

isPlaying = input('Would you like to play (R)ock, (P)aper, (S)cissors? ')

def compare(choice1, choice2):
	if choice1.lower() == choice2.lower():
		return "The result is a tie!"
	elif choice1 == 'P'.lower() and choice2 =='R'.lower():
		return "Player 1 wins!"
	elif choice2 == 'P'.lower() and choice1 == 'R'.lower():
		return "Player 2 wins!"
	elif choice1 == 'R'.lower() and choice2 == 'S'.lower():
		return "Player 1 wins!"
	elif choice2 == 'R'.lower() and choice1 == 'S'.lower():
		return "Player 2 wins!"
	elif choice1 == 'S'.lower() and  choice2 == 'P'.lower():
		return "Player 1 wins!"
	elif choice2 == 'S'.lower() and choice1 == 'P'.lower():
		return "Plater 2 wins!"

while isPlaying.lower() == 'y':
	choice1 = input('Player 1: Please enter either (R)ock, (P)aper, or (S)cissors: ')
	choice2 = input('Player 2: Please enter either (R)ock, (P)aper, or (S)cissors: ')
	print(compare(choice1,choice2))
	isPlaying = input('Would you like to play again? ')