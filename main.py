from telethon import TelegramClient
from telethon.sessions import StringSession
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_string = os.environ["SESSION_STRING"]

client = TelegramClient(StringSession(session_string), api_id, api_hash)

async def main():
    me = await client.get_me()
    print(f"Logged in as {me.first_name} ({me.id})")

with client:
    client.loop.run_until_complete(main())
