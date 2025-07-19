from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_string = os.environ["SESSION_STRING"]

source_channel_ids = [-1001002714330182]
target_channel_id = -1002840952584

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel_ids))
async def handler(event):
    message_text = event.raw_text
    await client.send_message(target_channel_id, message_text)

client.start()
client.run_until_disconnected()
