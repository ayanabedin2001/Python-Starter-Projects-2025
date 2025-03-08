import random

# creating choices
choices = ["rock", "paper", "scissor"]

computer_choices = random.choice(choices)

print("Enter 'exit' to quit.")



while True:
	#user inputs
	user_choice = input("Enter your choice: ")

	# display the choices
	print(f"Computer choice: {computer_choices}")
	print(f"User choice {user_choice}")

	# break the loop
	if user_choice == 'exit':
		print("Thanks for playing.")
		break
	# creating conditions
	if user_choice == computer_choices:
		print("It is a tie!")
	elif (user_choice == 'rock' and computer_choices == 'scissor') or (user_choice == 'paper' and computer_choices == 'rock') or (user_choice == 'scissor' and computer_choices == 'player'):
		print("Player wins!")
	else:
		print("Computer wins!")