# Gagik-Python
import random

def roll_dice():
    input("Press Enter to roll the dice...")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(f"You rolled {dice1} + {dice2} = {total}")
    return total

def play_craps():
    print("Welcome to Craps!")
    first_roll = roll_dice()

    if first_roll in [7, 11]:
        print("You win!")
    elif first_roll in [2, 3, 12]:
        print("Casino wins!")
    else:
        goal = first_roll
        print(f"Your goal is now {goal}. Keep rolling!")
        while True:
            roll = roll_dice()
            if roll == goal:
                print("You win!")
                break
            elif roll == 7:
                print("Casino wins!")
                break

if __name__ == "__main__":
        play_craps()

   

    
