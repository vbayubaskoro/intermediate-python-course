import random

def main():
	dice_rolls = 2
	dice_sum = 0
	for i in range(0,dice_rolls):
		roll = random.randint(1,6)
		dice_sum += roll 
		if roll == 1:
			print("You rolled a {}! Critical Fail".format(roll))
		elif roll == 6:
			print("You rolled a {}! Critical Success!".format(roll))
		else:
			print("You rolled a {}".format(roll))




if __name__== "__main__":
  main()