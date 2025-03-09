import random
import time

# create a function to simulate
def dice_roll():
	return random.randint(1, 6)

print("Rolling dice....")
# delay for 2 seconds
time.sleep(2)
print(f"You rolled a {dice_roll()}")