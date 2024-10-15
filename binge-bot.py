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

# Wait for the user to manually log in or you can add a login automation if needed
input("Please log in to Netflix and press Enter once you're on the episode page...")
input("How many episodes would you like to binge tonight?")

# Function to detect and click the "Next Episode" button
def click_next_episode():
    try:
        # Wait until the "Next Episode" button becomes visible (adjust timeout as needed)
        next_button = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Next Episode')]"))
        )
        next_button.click()
        print("Next Episode button clicked!")
    except Exception as e:
        print("Next Episode button not found. Error: ", str(e))

# Keep checking for the "Next Episode" button periodically (every few seconds)
while True:
    click_next_episode()
    time.sleep(60)  # Check every minute

