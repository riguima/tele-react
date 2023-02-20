from pyrogram import Client
from dotenv import load_dotenv
import os


load_dotenv()


app = Client(
    'tele_react_bot',
    api_id=os.getenv('API_ID'),
    api_hash=os.getenv('API_HASH'),
    bot_token=os.getenv('BOT_TOKEN'),
)


@app.on_message()
async def react(client, message):
    await app.send_reaction(message.chat.id, message.id, '🔥')


app.run()
