from telethon import TelegramClient, events
import os
from telethon.sessions import StringSession

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_string = os.environ["SESSION"]

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    if event.is_private:
        await event.reply("Привет, я живой!")

client.start()
client.run_until_disconnected()
