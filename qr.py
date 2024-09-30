import os
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import qrcode
from PIL import Image, ImageDraw, ImageOps

# Define bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Store the template image sent by the user
template_image_path = 'template.png'

# Start command handler
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Send me an image to use as the base for the QR code.")

# Handle image uploads
def handle_image(update: Update, context: CallbackContext):
    global template_image_path
    # Get the file from the message
    file = update.message.photo[-1].get_file()
    file.download(template_image_path)
    update.message.reply_text("Image received. Now send me the link/number to generate the QR code.")

# Handle text (links/numbers) and embed the QR code into the image
def handle_text(update: Update, context: CallbackContext):
    global template_image_path
    data = update.message.text  # The link or number to be encoded
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create QR code image (black and white)
    qr_img = qr.make_image(fill='black', back_color='white')
    
    # Open the template image
    try:
        template_img = Image.open(template_image_path).convert('RGBA')  # Keep alpha channel for transparency
    except FileNotFoundError:
        update.message.reply_text("Template image not found. Please send an image first.")
        return
    
    # Resize the QR code to fit the template image
    template_img = template_img.resize(qr_img.size)
    
    # Convert the QR code image to have transparency (RGBA)
    qr_img = qr_img.convert('RGBA')
    
    # Overlay the QR code onto the image: combine QR code and template image
    combined = Image.blend(template_img, qr_img, alpha=0.6)  # Adjust alpha to control transparency
    
    # Save the final image
    output_path = 'qr_embedded_template.png'
    combined.save(output_path)
    
    # Send the image back to the user
    with open(output_path, 'rb') as f:
        update.message.reply_photo(photo=InputFile(f))
    
    # Clean up the generated file
    os.remove(output_path)

# Main function to run the bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_image))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
