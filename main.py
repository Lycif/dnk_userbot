from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import requests

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_string = os.environ["SESSION_STRING"]
bot_token = os.environ["BOT_TOKEN"]

source_channel_id = -1001002714330182
target_channel_id = -1002840952584

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel_id))
async def handler(event):
    message_text = event.raw_text
    requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        data={"chat_id": target_channel_id, "text": message_text}
    )

client.start()
client.run_until_disconnected()
