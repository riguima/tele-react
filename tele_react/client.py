from pyrogram import Client
from pyrogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv('USERNAME'),
    api_id=os.getenv('API_ID'),
    api_hash=os.getenv('API_HASH'),
)

@client.on_message()
async def react(client: Client, message: Message) -> None:
    await client.send_reaction(message.chat.id, message.id, '❤️')
