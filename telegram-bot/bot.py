import os
import re
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Load environment variables from .env file
load_dotenv()
token = os.getenv('TELEGRAM_BOT_TOKEN')

# Function to start the bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bienvenido al bot de la libertad. Por favor, envíame tu cédula en el siguiente formato: V12345678, E12345678, J12345678 o P12345678.')

# Function to handle incoming messages
def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text.strip()
    
    # Regex to validate the cedula
    pattern = re.compile(r'^[VEJPvejp][0-9]{5,9}$')
    
    # Clean up the input
    cleaned_input = re.sub(r'[^0-9A-Za-z]', '', user_input).upper()
    
    if not cleaned_input[0].isdigit():
        if pattern.match(cleaned_input):
            # Call the endpoint with the cleaned cedula
            endpoint = f"https://tvtcrhau2vo336qa5r66p3bygy0hazyk.lambda-url.us-east-1.on.aws/?cedula={cleaned_input}"
            response = requests.get(endpoint)
            if response.status_code == 200:
                data = response.json()
                image_url = data.get('url')
                if image_url:
                    # Download the image
                    image_response = requests.get(image_url)
                    if image_response.status_code == 200:
                        image_path = 'acta.jpg'
                        with open(image_path, 'wb') as image_file:
                            image_file.write(image_response.content)
                        
                        # Send the image back to the user as a document
                        update.message.reply_document(document=open(image_path, 'rb'))
                    else:
                        update.message.reply_text('Lo siento, no se pudo descargar la imagen del acta.')
                else:
                    update.message.reply_text('Lo siento, no se encontró la URL de la imagen en la respuesta.')
            else:
                update.message.reply_text('Lo siento, hubo un error al consultar el acta en el servidor.')
        else:
            update.message.reply_text('Cédula no válida. Por favor, proporciona una cédula en uno de estos formatos: V12345678, E12345678, J12345678 o P12345678.')
    else:
        update.message.reply_text('La cédula debe empezar con V, E, J o P.')

def main() -> None:
    # Your bot token
    token = os.getenv('TELEGRAM_BOT_TOKEN')

    # Create the Updater and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register the message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
