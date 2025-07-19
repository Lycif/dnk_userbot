from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_string = os.environ["SESSION_STRING"]
bot_username = "genereytposters_bot"

keywords = ["шахеды", "БПЛА", "Ракети", "балістика", "Бій", "Усік", "Новини"]

channels = [
    "https://t.me/RLSukr",
    "https://t.me/+P8imXZKT0VIzMzRi",
    "https://t.me/noviyykanal"
]

client = TelegramClient(StringSession(session_string), api_id, api_hash)

def contains_keywords(text):
    return any(word.lower() in text.lower() for word in keywords)

@client.on(events.NewMessage(chats=channels))
async def handler(event):
    message = event.message
    if message.text and contains_keywords(message.text):
        await client.send_message(bot_username, message.text)

with client:
    client.run_until_disconnected()
