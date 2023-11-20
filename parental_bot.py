# Parental Bot
# Author: Josh
# Nov. 17, 2023

# Ask first question
print("Did you eat?")
kid = input().strip(" ").lower().split(" ")

# Ask second question
print("Did you study?")
kid = input().strip(" ").lower().split(" ")

# Ask third question
print("Did you do your laundry?")
kid = input().strip(" ").lower().split(" ")

# Ask fourth question
print("Did you call grandma?")
kid = input().strip(" ").lower().split(" ")

# Initialize our mom score
mom_score = 0

with open("./data.csv") as f:
    # Throw away the header line
    header = f.readline()

    # For every lineo f data in the file (string)
    for line in f:
        current_likes = line.split(",")
        