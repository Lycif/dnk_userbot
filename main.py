from telethon import TelegramClient
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_string = os.environ["SESSION"]

client = TelegramClient(StringSession(session_string), api_id, api_hash)

async def main():
    me = await client.get_me()
    print(f"UserBot запущен как @{me.username or me.first_name}")

with client:
    client.loop.run_until_complete(main())
