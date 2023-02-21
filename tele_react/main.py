from importlib import import_module
from pyrogram import idle
import asyncio

async def main():
    modules = [import_module('bot'), import_module('client')]
    for module in modules:
        await module.client.start()

    await idle()

    for module in modules:
        await module.client.stop()

if __name__ == '__main__':
    asyncio.run(main())
