from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
from domain import IRepository
from repositories import EmojiRepository, ChatRepository
import os


load_dotenv()


username = os.getenv('USERNAME')
emoji_repository = EmojiRepository()
chat_repository = ChatRepository()


@Client.on_message(filters.command('start') & filters.user(username))
async def start(client: Client, message: Message) -> None:
    text = ('/adicionar_emoji 🔥 - Adiciona o emoji 🔥 na lista\n'
            '/remover_emoji 🔥 - Remove o emoji 🔥 da lista\n'
            '/emojis - Mostra a lista dos emojis adicionados\n\n'
            '/adicionar_chat nome - Adiciona chat para fazer reações\n'
            '/remover_chat nome - Remove um chat\n'
            '/chats - Mostra a lista dos chats adicionados')
    await client.send_message(message.chat.id, text)


@Client.on_message(filters.command('adicionar_emoji') & filters.user(username))
async def add_emoji(client: Client, message: Message) -> None:
    emoji = message.text.split()[-1]
    emoji_repository.add(emoji)
    await client.send_message(message.chat.id, f'Emoji {emoji} adicionado!')


@Client.on_message(filters.command('remover_emoji') & filters.user(username))
async def remove_emoji(client: Client, message: Message) -> None:
    emoji = message.text.split()[-1]
    if emoji in emoji_repository.all():
        emoji_repository.delete(emoji)
        await client.send_message(message.chat.id, f'Emoji {emoji} removido!')
    else:
        await client.send_message(message.chat.id, 'Emoji não encontrado')


@Client.on_message(filters.command('emojis') & filters.user(username))
async def emojis(client: Client, message: Message) -> None:
    await client.send_message(message.chat.id, get_list(emoji_repository))


@Client.on_message(filters.command('adicionar_chat') & filters.user(username))
async def add_chat(client: Client, message: Message) -> None:
    chat = message.text.split()[-1]
    chat_repository.add(chat)
    await client.send_message(message.chat.id, f'Chat "{chat}" adicionado!')


@Client.on_message(filters.command('remover_chat') & filters.user(username))
async def remove_chat(client: Client, message: Message) -> None:
    chat = message.text.split()[-1]
    if chat in chat_repository.all():
        chat_repository.delete(chat)
        await client.send_message(message.chat.id, f'Chat {chat} removido!')
    else:
        await client.send_message(message.chat.id, 'Chat não encontrado')


@Client.on_message(filters.command('chats') & filters.user(username))
async def chats(client: Client, message: Message) -> None:
    await client.send_message(message.chat.id, get_list(chat_repository))


def get_list(repository: IRepository) -> str:
    result = ''
    for enum, key in enumerate(repository.all()):
        result += f'{enum + 1} - {key}\n'
    return result
