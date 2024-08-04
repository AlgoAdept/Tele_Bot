# Tele_Bot
# Vincenzo K-Drama Telegram Bot

This is a Telegram bot providing information about the Vincenzo K-Drama. 
The bot offers several commands to get details about the show, including cast, episodes, characters, and famous quotes.

## Features

- **/start** - Welcome message
- **/help** - List of available commands
- **/info** - Plot synopsis and image
- **/cast** - Information about the main cast
- **/episodes** - Information about episodes and an image
- **/characters** - List of main characters
- **/quotes** - Famous quotes from the show
- **/dubbed_episodes** - List of episodes available in Hindi with links

## Requirements

- Python 3.x
- `python-telegram-bot` library
- `python-dotenv` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/s8115p/Tele-Bot.git
   cd Tele-Bot
2. Create and activate a virtual environment (recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. Install the required packages:
   ```sh
   pip install -r requirements.txt

4. Create a .env file in the root directory with the following content:
    
   TOKEN=your-telegram-bot-token
