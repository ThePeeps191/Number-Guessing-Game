import random

def guessing_game():
	num = random.randint(1, 100)
	while True:
		i = int(input("Guess a number between one and one hundred:\n"))
		if i == num:
			print("You guessed correctly!")
			break
		elif i > num:
			print("You guessed too high. Try again.\n")
		else:
			print("You guessed too low. Try again.\n")

guessing_game()
