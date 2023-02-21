from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv('BOT_NAME'),
    api_id=os.getenv('API_ID'),
    api_hash=os.getenv('API_HASH'),
    bot_token=os.getenv('BOT_TOKEN'),
)

@client.on_message(filters.command('start') & filters.user(os.getenv('USERNAME')))
async def start(client: Client, message: Message) -> None:
    text = (f'Comandos\n\n'
            '/adicionar_emoji - Adiciona um emoji\n'
            '/remover_emoji - Remove um emoji\n'
            '/emojis - Mostra a lista dos emojis adicionados')
    await client.send_message(message.chat.id, text)
