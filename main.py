from telethon import events

@client.on(events.NewMessage)
async def get_chat_id(event):
    chat = await event.get_chat()
    print(f"Chat title: {chat.title}")
    print(f"Chat ID: {event.chat_id}")
