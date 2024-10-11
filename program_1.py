# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.

import random

def randDice():
    # Generate 2 random numbers between 1 and 6
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    # Sum the two numbers
    total = die1 + die2
    # Return the sum to the calling function
    return total

# Mainline
def main():
    rolls = []

    # Call randDice function 100 times
    for _ in range(100):
        rolls.append(randDice())

    # Calculate the average of the rolls
    average = sum(rolls) / len(rolls)

    # Print the average rounded to the nearest 0.01
    print(f"Average of 100 rolls: {average:.2f}")

if __name__ == "__main__":
    main()
