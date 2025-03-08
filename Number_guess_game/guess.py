import random

# decalring number and guess variable
guess = None
number = random.randint(1, 20)

# creating the logic
# creating a for loop to keep the program running until guessed
while guess != number:
	try:
		guess = input("Guess a number between 1 and 20: ")
		guess = int(guess)
		if guess == number:
			print("You guessed it right. You won!")
		elif guess < number:
			print("Too low guess. Guess higher!")
		else:
			print("Too high guess. Guess a little lower!")
	except ValueError:
		print("Try again!")
	

print("You won!")