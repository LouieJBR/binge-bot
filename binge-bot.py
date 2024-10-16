# Binge Bot

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome browser (or whichever browser you're using)
driver = webdriver.Chrome()

# Open Netflix (you might need to login manually or automate it)
driver.get("https://www.netflix.com")

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

# Wait for the user to manually log in or you can add a login automation if needed
input("Please log in to Netflix and press Enter once you're on the episode page...")
numEpisodes = int(input('How many episodes would you like to watch tonight? '))  # Convert input to int

print(f'Awesome! BingeBot will continue running for {numEpisodes} episodes.')

episodesWatched = 0
# Function to detect and click the "Next Episode" button
def click_next_episode():
    try:
        # Wait until the "Next Episode" button becomes visible (adjust timeout as needed)
        next_button = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Next Episode')]"))
        )
        next_button.click()
        episodesWatched += 1
        print("Next Episode button clicked!")
    except Exception as e:
        print("Next Episode button not found. Error: ", str(e))

# Keep checking for the "Next Episode" button periodically (every few seconds)
while episodesWatched < numEpisodes:
    click_next_episode()
    time.sleep(20)  # Check every minute

