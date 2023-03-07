from pyrogram import Client, filters
from pyrogram.types import Message
from random import choice
from repositories import EmojiRepository, ChatRepository

emoji_repository = EmojiRepository()
chat_repository = ChatRepository()

@Client.on_message()
async def react(client: Client, message: Message) -> None:
    if emoji_repository.all() and message.chat.title in chat_repository.all():
        await client.send_reaction(message.chat.id, message.id, choice(emoji_repository.all()))
