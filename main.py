from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import requests

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_string = os.environ["SESSION_STRING"]
bot_token = "8158303139:AAHligZP-v29MPZE3YLuUj0wwsM1Cw8lp_w"
bot_username = "genereytposters_bot"

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage(chats=[1002714330182]))
async def handler(event):
    text = event.raw_text
    print("Поймал сообщение:", text)
    
    requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        data={"chat_id": "@"+bot_username, "text": text}
    )

with client:
    client.run_until_disconnected()
