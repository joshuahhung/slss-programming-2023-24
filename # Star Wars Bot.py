# Star Wars Bot
# Author: Josh
# Date: 16 October 2023

import random
import time

# Greet the user
print("A long time ago")
time.sleep(1.5)
print("in a galaxy far far away...")
time.sleep(2)

# Introduce yourself
print("Where your focus determines your reality...")
time.sleep(1)
print("The force is what gives a Jedi his power.")
time.sleep(1)
print("While fear is the path to the dark side.")
time.sleep(2)
print("choose wisely...")

# Question if the user likes capes or not
cape = input("so, do you like capes? ")
time.sleep(1)

# if they do, reply with 
if cape.lower() == "yes":
    print("hm... okay, its still too early to tell")
elif cape.lower() == "no":
    print("That's great.🤖")


# Question the user to see if which side they are
fav_color = input("Do you like the color blue or green? ")
time.sleep(1)

# If their favourite color is blue or green, reply with the force is strong with you. 
if fav_color.lower() == "blue": 
    print("The force is strong with you")
elif fav_color.lower() == "green":
    print("Not bad, I think blue is cooler through")
else:
    # Create a lsit of possible responses
    fav_colors = [
        f"hm... I suppose purple could be an option",
    ]

# Ask them another question
fav_color_red = input("Do you like the color red? ")
time.sleep(1)

# list possible responses to whether they are in the light side or dark side.
if fav_color_red.lower() == "yes":
    print("wha- you were supposed to be the chosen one!")
    print("you were like a bruddah to me!")
    print("You've become the very thing you swore to destroy!")
elif fav_color_red.lower() == "no":
    print("alright. cool. I'm chill wit dat")
    print("Light side it is")