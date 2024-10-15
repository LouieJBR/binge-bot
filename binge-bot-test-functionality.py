import time

# This is a logic test, no webdriver functionality here.
# TEST USER SPECIFY HOW MANY EP TO BINGE

binge_bot = r"""
+------------------+
|     Binge Bot    |
|                  |
|       .---.      |
|      |     |     |
|     /       \    |
|    |   O O   |   |    
|    |    -    |   |
|     \_______/    |
|      /     \     |
|     |       |    |
|     |_______|    |
|                  |
|   Next Episode   |
|      Loading...  |
+------------------+
"""
print(binge_bot)

numEpisodes = int(input('How many episodes would you like to watch tonight? '))  # Convert input to int

print(f'Awesome! BingeBot will continue running for {numEpisodes} episodes.')

episodesWatched = 0

def clickNextEpisode():
    global episodesWatched  # Declare episodesWatched as global to modify it inside the function
    print(f"Next Episode button clicked {episodesWatched+1} times!")
    episodesWatched += 1

while episodesWatched < numEpisodes:  # Change to < to continue until numEpisodes is reached
    clickNextEpisode()
    time.sleep(5)  # Check every 5s
