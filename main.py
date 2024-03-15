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
            caption=f"𝐇𝐞𝐲..! {user_fullname} ❤️\n\n𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐢𝐦𝐚𝐠𝐞, 𝐚𝐧𝐝 𝐈'𝐥𝐥 𝐮𝐩𝐥𝐨𝐚𝐝 𝐢𝐭 𝐭𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 𝐚𝐧𝐝 𝐩𝐫𝐨𝐯𝐢𝐝𝐞 𝐲𝐨𝐮 𝐚 𝐝𝐢𝐫𝐞𝐜𝐭 𝐥𝐢𝐧𝐤.\n\n𝐒𝐇𝐀𝐑𝐄 & 𝐒𝐔𝐏𝐏𝐎𝐑𝐓\n@𝐓𝐀𝐃𝐱𝐁𝐨𝐭𝐳 ❤️"
        )

# Handler for receiving photo messages
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    try:
        # Send a "Please wait" message
        wait_message = bot.reply_to(message, "𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭, 𝐲𝐨𝐮𝐫 𝐢𝐦𝐚𝐠𝐞 𝐢𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠...")

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
                f"𝐈𝐦𝐚𝐠𝐞 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲::\n\n"
                f"𝟏𝐬𝐭:\n{uploaded_url}\n\n"
                f"2𝐧𝐝:\nhttp://telegra.ph/file/{uploaded_filename}\n\n"
                f"𝐉𝐨𝐢𝐧 @TADxBotz ❤️"
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
    bot.reply_to(message, "𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐨𝐧𝐥𝐲 𝐢𝐦𝐚𝐠𝐞𝐬. 𝐎𝐭𝐡𝐞𝐫 𝐟𝐢𝐥𝐞 𝐭𝐲𝐩𝐞𝐬 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐬𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝.")

# Start the bot
bot.polling()
