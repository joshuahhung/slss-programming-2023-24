# Functions Practice
# Author: Josh
# 24 November 2023


def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    return area


def print_area_of_a_square(sidelength: float) -> None:
    """Calculate and print the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    print(
        f"The area of a square with side length {sidelength} is: {area} square units."
    )


print(print_area_of_a_square(12.2))
# print_area_of_a_square(12)

# Given two squares of two sidelengths
#    12.2 and 144
# Add the area of both squares

# area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
# print(area_of_squares)





# Question 1
# Write a function called stars()
# It takes an int as a parameter 
# It returns a string of stars with the same length as the argument.

def stars(num_stars: int) -> str:
    """Returns a number of stars
    
    Params:

    num_stars - the number of stars to return
    """

    return "*" * num_stars

print(stars(10000))


# Question 2
# Write a function that takes 3 numbers
# It should return the biggest of the three numbers.
# Call it biggest_of_three()
# Don't use the builtin max() function
def biggest_of_three(num_one: int, num_two: int, num_three: int) -> str:
    """Returns the biggest of the three numbers
    Params:

    three - the number of the biggest number to return 
    """
    if num_one >= num_two and num_one >= num_three:
        return num_one
    elif num_two >= num_two and num_one >= num_three:
        return num_two
    else:
        return num_three
    
print(biggest_of_three())