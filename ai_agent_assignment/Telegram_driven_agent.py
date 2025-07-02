

# Telegram AI Agent for Automated Posting to groups and channels
# Requires: pip install requests
# Fill in your API credentials below
import requests

TELEGRAM_BOT_TOKEN = "7777805272:AAH-qkjJdk5x19neX91KWbEwOX3x6t82bMA"
TELEGRAM_CHAT_ID = "-1002777863370"  # Can be user, group, or channel ID

def send_telegram_message(text):
    """Send a message to a Telegram chat using the bot."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message: {response.text}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Example usage:
send_telegram_message("Dear group members, the Premier League season is starting next month! Get ready for exciting matches and updates. Stay tuned!")
