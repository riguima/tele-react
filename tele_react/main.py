from pyrogram import idle, Client
import asyncio
import os
from dotenv import load_dotenv


async def main():
    load_dotenv()
    apps = [
        Client(
            os.getenv('USERNAME'),
            api_id=os.getenv('API_ID'),
            api_hash=os.getenv('API_HASH'),
            plugins=dict(root='client_plugins', include=['handlers'])),
        Client(
            os.getenv('BOT_NAME'),
            api_id=os.getenv('API_ID'),
            api_hash=os.getenv('API_HASH'),
            bot_token=os.getenv('BOT_TOKEN'),
            plugins=dict(root='bot_plugins', include=['handlers'])),
    ]
    for app in apps:
        await app.start()

    await idle()

    for app in apps:
        await app.stop()


if __name__ == '__main__':
    asyncio.run(main())
