import random
import time

dice_min = 1
dice_default = 6

while True:
    dice_user = input(f"How many sides do you want? Default value is six. ")
    try:
        dice_user = int(dice_user)
        if dice_user < dice_min:
            print(f"Sorry, the number of sides must be at least {dice_min}.")
        else:
            break
    except ValueError:
        print("Give me a number.")


print(f"Sides of the dice: {dice_user}")


def dice_throwing():
    return random.randint(dice_min, dice_user)

def delay():
    print("Dice is rolling...")
    time.sleep (3.0)

while True:
    throw = input("Do you throw the dice? (Y/N)  ")
    if throw == "Y" or throw == "y" or throw == "Yes" or throw == "yes":
        delay()
        print(dice_throwing())
    elif throw == "N" or throw == "n" or throw == "No" or throw == "no":
        print("Bye!")
        break
    else:
        print('Invalid input! Only "Yes" or "No" [Y/N] accepted.')