from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
from repositories import EmojiRepository
import os


load_dotenv()


username = os.getenv('USERNAME')
emoji_repository = EmojiRepository()


@Client.on_message(filters.command('start') & filters.user(username))
async def start(client: Client, message: Message) -> None:
    text = ('/adicionar_emoji 🔥 - Adiciona o emoji 🔥 na lista\n'
            '/remover_emoji 🔥 - Remove o emoji 🔥 da lista\n'
            '/emojis - Mostra a lista dos emojis adicionados')
    await client.send_message(message.chat.id, text)


@Client.on_message(filters.command('adicionar_emoji') & filters.user(username))
async def add_emoji(client: Client, message: Message) -> None:
    emoji = message.text.split()[-1]
    emoji_repository.add(emoji)
    await client.send_message(message.chat.id, f'Emoji {emoji} adicionado!')


@Client.on_message(filters.command('remover_emoji') & filters.user(username))
async def remove_emoji(client: Client, message: Message) -> None:
    emoji = emoji_repository.get(message.text.split()[-1])
    if emoji:
        emoji_repository.delete(emoji)
        await client.send_message(message.chat.id, f'Emoji {emoji} removido!')
    else:
        await client.send_message(message.chat.id, 'Emoji não encontrado')


@Client.on_message(filters.command('emojis') & filters.user(username))
async def emojis(client: Client, message: Message) -> None:
    await client.send_message(message.chat.id, get_emojis())


def get_emojis() -> str:
    result = ''
    for enum, emoji in enumerate(emoji_repository.all()):
        result += f'{enum + 1} - {emoji}\n'
    return result
