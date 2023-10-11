# loop practice
# author: Josh
# date: 2023-10-10

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games", "carrots"]

# Do something for each thing in the list
# Print it out in a pretty way
# e.g.
#     * hot wheels
#       ---
#     * lego
#       ---
#       etc.

# print(f"* {groceries[0]}")
# print(f"  ---")
# print(f"* {groceries[1]}")
# print(f"  ---")
# print(f"* {groceries[2]}")
# print(f"  ---")

for item in groceries:
    print(f"* {item}")
    print(f"  ---")

# Using the above method, create the thing below:
# *
# **
# ***
# ****
# *****
# ******

pyramid = ["*", "**", "***", "****", "*****", "******"]

for row in pyramid:
    print(f"* {row}")

import time

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
for number in countdown:
    print(number)
    time.sleep(1)

print("Happy New Year!")
