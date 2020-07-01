import random

def main():
	dice_rolls = int(input("How many dice would you like to roll? "))
	dice_size = int(input("How many sides are the dice? "))
	dice_sum = 0
	for i in range(0,dice_size):
		roll = random.randint(1,6)
		dice_sum += roll 
		if roll == 1:
			print("You rolled a {}! Critical Fail".format(roll))
		elif roll == dice_size:
			print("You rolled a {}! Critical Success!".format(roll))
		else:
			print("You rolled a {}".format(roll))
	print("You have rolled a total of {}".format(dice_sum))




if __name__== "__main__":
  main()