import os
import requests
import telebot
import time
from config import *

# Initialize the bot using the token from config.py
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# File path of the welcome image
welcome_image_path = IMG_PATH

# Command handler for /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Get user's full name
    user_fullname = message.from_user.first_name + ' ' + message.from_user.last_name if message.from_user.last_name else message.from_user.first_name

    # Send personalized welcome message with the image
    with open(welcome_image_path, 'rb') as photo:
        bot.send_photo(
            message.chat.id,
            photo,
            caption=f"Hey..! {user_fullname}❤️\n\nSend me any image, and I'll upload it to Telegraph and provide you a direct link.\n\nSHARE & SUPPORT\n@TADxBotz ❤️"
        )

# Handler for receiving photo messages
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    try:
        # Send a "Please wait" message
        wait_message = bot.reply_to(message, "Please wait, your image is uploading...")

        # Get the image file ID
        file_id = message.photo[-1].file_id

        # Get the image file
        file_info = bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"

        # Download the image file
        local_filename = f"{file_id}.jpg"
        with requests.get(file_url) as response:
            with open(local_filename, 'wb') as f:
                f.write(response.content)

        # Upload the image to Te.legra.ph
        with open(local_filename, 'rb') as f:
            response = requests.post('https://te.legra.ph/upload', files={'file': f})

        if response.status_code == 200:
            # Get the uploaded image URL
            uploaded_filename = response.json()[0]['src'].split('/')[-1]
            uploaded_url = f"https://te.legra.ph/file/{uploaded_filename}"
            
            # Prepare the message
            message_text = (
                f"Image uploaded successfully:\n\n"
                f"1st:\n{uploaded_url}\n\n"
                f"2nd:\nhttp://telegra.ph/file/{uploaded_filename}\n\n"
                f"Join @TADxBotz ❤️"
            )
            
            # Reply to the user without showing preview
            sent_message = bot.reply_to(message, message_text, disable_web_page_preview=True)

            # Delete the "Please wait" message
            bot.delete_message(chat_id=wait_message.chat.id, message_id=wait_message.message_id)

            # Delete the local image file
            os.remove(local_filename)
        else:
            bot.reply_to(message, "Failed to upload image.")

    except Exception as e:
        print(e)
        bot.reply_to(message, "An error occurred while processing the image.")

# Handler for unsupported file types
@bot.message_handler(content_types=['document', 'audio', 'video', 'voice', 'sticker'])
def handle_other_files(message):
    bot.reply_to(message, "Please send only images. Other file types are not supported.")

# Start the bot
bot.polling()
