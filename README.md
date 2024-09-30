*QR Code Embedder Bot*

A Telegram bot that embeds QR codes into user-provided images.


*Table of Contents*

1. #overview
2. #features
3. #requirements
4. #installation
5. #usage
6. #license
7. #contributing


*Overview*

This bot uses the Telegram API and Python libraries (Pillow, qrcode, and python-telegram-bot) to generate QR codes and overlay them onto user-provided images.


*Features*

- Accepts images from users as templates
- Generates QR codes from user-provided text (links or numbers)
- Overlays QR codes onto template images with adjustable transparency
- Sends the resulting image back to the user


*Requirements*

- Python 3.8+
- Pillow
- qrcode
- python-telegram-bot
- Telegram Bot API token


*Installation*

1. Clone the repository: `git clone https://github.com/Keyz400/image-qr-code-telegram-bot`
2. Install dependencies: `pip3 install -r requirements.txt`
3. Replace `YOUR_BOT_TOKEN` with your actual Telegram Bot API token in `qr.py`
4. Run the bot: `python3 qr.py`


*Usage*

1. Start the bot: `/start`
2. Send an image as the template
3. Send the link/number to generate the QR code



*Authors*
Black
