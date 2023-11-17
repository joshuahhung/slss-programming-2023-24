# Similarity Score
#
#

josh_fave_movies = [
    "Back To The Future",
    "Indiana Jones: The Last Crusader",
    "Toy Story 2",
    "Avengers: Infinity War",
    "Saving Private Ryan"
]

ubials_fave_movies = [
    "Matrix",
    "Star Wars Episode 5: The Empire Strikes Back",
    "Avengers: Infinity War",
    "Toy Story 2",
    "The Intouchables"
]

similarity_score = 0

# Sim Score Algorithm
for movie in josh_fave_movies:
    if movie in ubials_fave_movies:
        similarity_score += 1

print(f"Josh has {similarity_score} movies in common.")

print("Josh has " + str(similarity_score) + " movies in common.")