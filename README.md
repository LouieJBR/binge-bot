# BingeBot

**BingeBot** is a Python-based automation tool that automatically clicks the "Next Episode" button on streaming platforms like Netflix, allowing for a seamless binge-watching experience. 

## Features

- Detects when the "Next Episode" button appears on a streaming service.
- Automatically clicks the button to move on to the next episode without manual intervention.
- Supports automation using Selenium or PyAutoGUI for different setups.

## Installation

### Prerequisites:
- Python 3.x
- [Google Chrome](https://www.google.com/chrome/) (if using Selenium)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (for Selenium users)

### Setup:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/BingeBot.git
   cd BingeBot
   ```

2. Install the required packages:
   - For Selenium:
     ```bash
     pip install selenium
     ```
   - For PyAutoGUI:
     ```bash
     pip install pyautogui
     ```

3. If using Selenium, download the correct WebDriver for your browser and ensure it's in your PATH.

## Usage

1. Start the script:
   ```bash
   python bingebot.py
   ```

2. Log in to your preferred streaming service manually.

3. BingeBot will automatically detect and click the "Next Episode" button when it appears.
