# Similar Hobbies
# Author: Josh
# 14 November, 2023

# Get user one's hobbies
print("What're your hobbies?")
josh_hobbies = input().strip(",.?! ").lower().split(" ")

# Convert user one's hobbies into a list


# Get user two's hobbies

# Convert user two's hobbies into a list
print("What're your hobbies?")
ubial_hobbies = input().strip(",.?! ").lower().split(" ")

similarity_score = 0
# Apply the similarity score algo to the two lists
for hobbie in josh_hobbies:
    if hobbie in ubial_hobbies:
        similarity_score += 1

# Print the results
print(f"Josh has {similarity_score} hobbies in common.")