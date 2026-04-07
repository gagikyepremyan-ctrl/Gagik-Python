import random

def roll_dice():
    
    numbers = [1, 2, 3, 4, 5, 6]
    die1 = random.choice(numbers)
    die2 = random.choice(numbers)
    total = die1 + die2
    print(f"You rolled {die1} and {die2} = {total}.")

    if die1 + die2 in [7, 11]:
        print("Congratulations! You win!")
    elif total in [2, 3, 12]:
        print("Craps! The casino wins.")
    else:
        goal = total
        print(f"Your goal is to roll a {goal} again before rolling a 7.")
        while True:
            input("Press Enter to roll the dice again...")
            die1 = random.choice(numbers)
            die2 = random.choice(numbers)
            total = die1 + die2
            print(f"You rolled {die1} and {die2} = {total}.") 
            if total == goal:
                print("Congratulations! You win!")
                break
            elif total == 7:
                print("You rolled a 7. The casino wins.")
                rotate_dice()
                break

def rotate_dice():
    print("Rolling the dice again...")
    roll_dice()
if __name__ == "__main__":
    print("Welcome to the Craps Game!")
    roll_dice()
    