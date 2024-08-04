import telegram.ext
from dotenv import load_dotenv
import os

# Load the bot token from the .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Define command handlers
def start(update, context):
    update.message.reply_text("Hello! Welcome to the Vincenzo K-Drama Bot. Type /help to see available commands.")

def helps(update, context):
    update.message.reply_text("""
    Hello There!
    I'm a chatbot providing information about the Vincenzo K-Drama.
    Here are some commands you can use:

    /start - to start the conversation
    /info - information about Vincenzo 
    /cast - information about the cast
    /episodes - information about episodes
    /characters - information about main characters
    /quotes - famous quotes from Vincenzo
    /dubbed_episodes - list of episodes available in Hindi dubbed version
    /help - to get this help menu

    Hope this helps you enjoy the show!
    """)

def info(update, context):
    update.message.reply_text("""
    **Plot Synopsis:**

    Vincenzo Cassano (Song Joong-Ki) is a Korean-Italian lawyer who works for the mafia as a consigliere. 
    After a power struggle within the mafia, he returns to South Korea and gets involved with lawyer Hong Cha-Young (Jeon Yeo-Bin). 
    Together, they work to bring justice by unconventional means.

    *Plot Image:* 
    """)
    context.bot.send_photo(chat_id=update.message.chat_id, photo='https://asianwiki.com/images/0/01/Vincenzo-KD-p1.jpg', caption="Vincenzo K-Drama Plot")


def cast(update, context):
    # Text description of the cast
    update.message.reply_text("""
    **Main Cast:**

    - *Song Joong-Ki* as Vincenzo Cassano
    - *Jeon Yeo-Bin* as Hong Cha-Young
    - *Ok Taec-Yeon* as Jang Jun-Woo
    - *Kim Yeo-Jin* as Choi Myung-Hee
    - *Kang Bu-ja* as Hong Yu-chan
    """)


def episodes(update, context):
    update.message.reply_text("""
    **Episodes Information:**

    The show consists of 20 episodes in total, with each episode running for approximately 70 minutes. 
    The drama aired from February 20, 2021, to May 2, 2021.
    """)
    context.bot.send_photo(chat_id=update.message.chat_id, photo='https://asianwiki.com/images/7/75/Vincenzo_Episodes.jpg', caption="Episodes Details")

def characters(update, context):
    update.message.reply_text("""
    **Main Characters:**

    - *Vincenzo Cassano* (Song Joong-Ki): A Korean-Italian mafia lawyer who seeks justice in his own way.
    - *Hong Cha-Young* (Jeon Yeo-Bin): A fiercely competitive lawyer who teams up with Vincenzo.
    - *Jang Jun-Woo* (Ok Taec-Yeon): A young CEO with hidden agendas.
    - *Choi Myung-Hee* (Kim Yeo-Jin): A villainous attorney involved with the mafia.
    """)
    context.bot.send_photo(chat_id=update.message.chat_id, photo='https://asianwiki.com/images/5/55/Vincenzo_Characters.jpg', caption="Main Characters")

def quotes(update, context):
    update.message.reply_text("""
    **Famous Quotes:**

    - "You either die a hero, or you live long enough to see yourself become the villain."
    - "In this world, it's not enough to be right. You have to be ready to fight."
    - "Justice isn't something you can just talk about; it's something you have to fight for."
    """)
    context.bot.send_photo(chat_id=update.message.chat_id, photo='https://asianwiki.com/images/4/4b/Vincenzo_Quotes.jpg', caption="Quotes from Vincenzo")

def dubbed_episodes(update, context):
    # List of episodes with their Hindi dubbed links
    episodes_in_hindi = {
        "Episode 1": "https://momerybox.com/s/1QaKeYblZw5Mi4YgZHkZsTA",
        "Episode 2": "https://momerybox.com/s/1_EfidvfSjQm580Mh8_TcvA",
        "Episode 3": "https://momerybox.com/s/1lS7JqqWTT1OOheYqdTC5ZA",
        "Episode 4": "https://momerybox.com/s/1KhpsRbKfHGYxnjTE2yZuiQ",
        "Episode 5": "https://momerybox.com/s/1sV7eioxcDmxGdbhpg2vWWQ",
        "Episode 6": "https://momerybox.com/s/1dBDbwCjqyr2xp2sVKzW3YQ",
        "Episode 7": "https://momerybox.com/s/1NF_iiLhKffTXAWRN9sMtxQ",
        "Episode 8": "https://momerybox.com/s/1bnLnq1obqx1_wGyEO_2e_A",
        "Episode 9": "https://momerybox.com/s/1gnp9B4aEStPWQSpNtywdrQ",
        "Episode 10": "https://momerybox.com/s/1V3TqLaLpVAngXULjOi6Dgg",
        "Episode 11": "https://momerybox.com/s/1Muejg2LGSaz5DfOO6PvG0g",
        "Episode 12": "https://momerybox.com/s/1CIIwJaGKjs_RiW6SYUN-DQ",
        "Episode 13": "https://momerybox.com/s/1zyrSr53AtlnR7hBmuR1zYA",
        "Episode 14": "https://momerybox.com/s/1sTMvPT3AsOodJK-QCu2AbA",
        "Episode 15": "https://momerybox.com/s/1hcp7nEZ87KtUhkj8BasW4Q",
        "Episode 16": "https://momerybox.com/s/1cwMPMRWs2TACf120DzJ6Xg",
        "Episode 17": "https://momerybox.com/s/129tIpuN4O-UC1V63IPz1sA",
        "Episode 18": "https://momerybox.com/s/1NNVfZUpw7gFfDpai-cUAnw",
        "Episode 19": "https://momerybox.com/s/1kNAuIVd9YlMa523YxH_mag",
        "Episode 20": "https://momerybox.com/s/1KB9vRnyXLqH0zQj789B3BQ"
    }

    response = "Here is the list of Vincenzo episodes available in Hindi dubbed version:\n\n"
    for episode, link in episodes_in_hindi.items():
        response += f"{episode}: [Watch here]({link})\n"

    update.message.reply_text(response, parse_mode=telegram.ParseMode.MARKDOWN)

# Create the updater and dispatcher
updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add handlers for commands
dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', helps))
dispatcher.add_handler(telegram.ext.CommandHandler('info', info))
dispatcher.add_handler(telegram.ext.CommandHandler('cast', cast))
dispatcher.add_handler(telegram.ext.CommandHandler('episodes', episodes))
dispatcher.add_handler(telegram.ext.CommandHandler('characters', characters))
dispatcher.add_handler(telegram.ext.CommandHandler('quotes', quotes))
dispatcher.add_handler(telegram.ext.CommandHandler('dubbed_episodes', dubbed_episodes))

# Start polling
updater.start_polling()
updater.idle()
