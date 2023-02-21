from pyrogram import Client, filters
from pyrogram.types import Message
from random import choice
from repositories import EmojiRepository

emoji_repository = EmojiRepository()

@Client.on_message(~ filters.private)
async def react(client: Client, message: Message) -> None:
    if emoji_repository.all():
        await client.send_reaction(message.chat.id, message.id, choice(emoji_repository.all()))
