import random

score = 0

print("Welcome to Treasure Hunt!")

# Function to get valid input

def get_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().capitalize()
        if choice in valid_choices:
            return choice
        else:
            print(f"Invalid choice! Please choose from {', '.join(valid_choices)}.")

# First Choice
# If the player chooses Left, the game ends.If they choose Right, they get 10 points and continue.


first_choice = get_choice("Choose your path (Left or Right): ", ["Left", "Right"])

if first_choice == "Left":
    print("Game Over! You fell into a hidden pit. Better luck next time...")
    exit()
else:
    score += 10
    print(f"Good choice! A signpost ahead reads: 'Follow the river, but beware of deep waters.' (+10 points)")
    print(f"Your score: {score}")

# Second Choice

second_choice = get_choice("Do you follow the River or take the Bridge? (River/Bridge): ", ["River", "Bridge"])

if second_choice == "River":
    print("Game Over! You slipped on a rock and got carried away by the current.")
    exit()
else:
    score += 10
    print(f"Smart move! The bridge was old, but it held firm. You see a cave in the distance. (+10 points)")
    print(f"Your score: {score}")

# Third Choice

third_choice = get_choice("Do you enter the Cave or explore the Forest? (Cave/Forest): ", ["Cave", "Forest"])

if third_choice == "Forest":
    print("Game Over! You got lost in the thick woods and were never seen again...")
    exit()
else:
    score += 10
    print(f"You found a hidden passage inside the cave leading to a dark hallway. You hear faint sounds ahead. (+10 points)")
    print(f"Your score: {score}")

# Fourth Choice (Random Event)
# This randomly determines if the player encounters danger or gets lucky.


print("You notice two paths ahead, but you hear strange noises...")
random_event = random.choice(["safe", "trap"])

fourth_choice = get_choice("Do you follow the Sound or take the Silent path? (Sound/Silent): ", ["Sound", "Silent"])

if fourth_choice == "Sound":
    if random_event == "trap":
        print("Oh no! The sounds were from a pack of wolves that attack you. You didn’t survive...")
        exit()
    else:
        score += 15
        print(f"You followed the sound and found a guide who leads you safely through the cave! (+15 points)")
        print(f"Your score: {score}")
else:
    score += 10
    print(f"Good thinking! The silent path leads to a torch-lit chamber with two doors. (+10 points)")
    print(f"Your score: {score}")

# Fifth Choice

fifth_choice = get_choice("Do you open the Golden Door or the Wooden Door? (Golden/Wooden): ", ["Golden", "Wooden"])

if fifth_choice == "Golden":
    print("The golden door was a trap! You took the treasure but were cursed forever! 👻")
    print(" Cursed Ending! Your greed led to your downfall.")
    exit()
else:
    score += 20
    print("You enter the wooden door and find a treasure chest!  (+20 points)")
    print(f"Final Score: {score}")

# Final Ending Based on Score
# **Multiple Endings Based on Score**

if score >= 50:
    print("TREASURE HUNTER ENDING: You became the richest adventurer of all time!")
elif score >= 40:
    print(" HERO ENDING: You defeated an ancient guardian and earned eternal glory!")
elif score >= 30:
    print(" SURVIVOR ENDING: You barely escaped, but at least you're alive.")
else:
    print(" BAD ENDING: You found nothing and were lost forever...")


# The final score determines the ending message.

# GOMBARUME TAPIWA
