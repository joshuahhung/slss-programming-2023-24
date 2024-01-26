# Spotify Data 
# Author: Josh
# 16 Jan 2024

import csv

# Open file
with open("./spotify.csv") as f:
    # ----- Search for all Drake songs
    # ----- Use linear search
    # Create a csv reader object
    csv_reader = csv.DictReader(f)   

    # Make a list to store all of Drake songs
    drake_songs = []

# Create a counter to store the current line number
    line_num = 0

    # For every line in the file
    for line in csv_reader:
        # If its the first line, print all the headings
        if line_num == 0:
            # print("The columns are: ")
            # Print on one line
            # print(", ".join(line))
             # Print one on every line
            

            line_num += 1
        else:
            # If artist for this song is drake
            # Store the song info in the list
            # ----- artist, song title, danceability
            if "drake" in line["artist"].lower():
                drake_songs.append((
                    line["artist"],
                    line["song_title"],
                    line["valence"],
                    line["danceability"]
                ))
            line_num += 1

print(drake_songs)