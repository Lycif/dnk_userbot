from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_string = os.environ["SESSION_STRING"]

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_chat()
    print(f"Название чата: {sender.title}")
    print(f"Chat ID: {sender.id}")

client.start()
client.run_until_disconnected()
