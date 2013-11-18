number = 10
numAttempts = 0

name = input("Hello!  What is your name? ")
print("Well,", name, "I am thinking of a number between 1 and 20.")

for i in [0, 1, 2]:
	guess = int(input("Take a guess. "))
	numAttempts = numAttempts + 1
	if guess == number:
		print("Your guess is correct and you guessed it in", numAttempts, "attempts!")
		break;
	if guess < number:
		print("Your guess is too low!")
	if guess > number:
		print("Your guess is too high!")
	if numAttempts >= 3:
		print("Your three guesses are over. The number I was thinking of was 10.")