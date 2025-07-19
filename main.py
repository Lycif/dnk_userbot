from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import requests

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_string = os.environ["SESSION_STRING"]

client = TelegramClient(StringSession(session_string), api_id, api_hash)

bot_token = "8158303139:AAHligZP-v29MPZE3YLuUj0wwsM1Cw8lp_w"
channel_id = 1002714330182

@client.on(events.NewMessage(chats=[channel_id]))
async def handler(event):
    message_text = event.raw_text
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": "@genereytposters_bot",
        "text": message_text
    }
    requests.post(url, data=data)

with client:
    client.run_until_disconnected()
