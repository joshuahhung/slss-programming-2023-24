# Bubble Tea Popularity Algorithm
# Author: Ubial
# Date: 27 October 2023

# Ask 5 users what their favourite bubble tea place is
# prints out a summary of the data

# ------ CONSTANTS

NUM_RESPONDENTS = 5


coco_likes = 0 # Initialize the variable to 0
suntea_likes = 0 
chatime_likes = 0
bubqueen_likes = 0


for _ in range(NUM_RESPONDENTS):

    # Ask the user what their favourite place is
    print("what's your favourite bubble tea place? ")

    fave_place = input( ).strip(",.?!").lower()

    # Tally or counting algo
    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "bubble queen":
        bubqueen_likes += 1

# Repeat the code above 5 times

# Print out a summary of all places
# Give the raw score AND the percentage

# Summary of Coco
print(f"CoCo Likes: {coco_likes}")
print(coco_likes/NUM_RESPONDENTS * 100)

# Summary of Suntea
print(f"Suntea Likes: {suntea_likes}")
print(suntea_likes/NUM_RESPONDENTS * 100)

# Summary of Chatime
print(f"Chatime Likes: {chatime_likes}")
print(chatime_likes/NUM_RESPONDENTS * 100)

# Summary of Bubqueen
print(f"Bubqueen Likes: {bubqueen_likes}")
print(bubqueen_likes/NUM_RESPONDENTS * 100)