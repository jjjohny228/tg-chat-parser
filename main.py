import os
from pyrogram import Client, filters, types
from pyrogram.handlers import MessageHandler
from dotenv import load_dotenv

from custom_filters import banned_words_filter, target_words_filter
from config import ban_words, target_chats, target_wards

load_dotenv()

app = Client('mark_account')

banned_words_filter = banned_words_filter(ban_words)
target_words_filter = target_words_filter(target_wards)


async def forward_client_messages(client: Client, message: types.Message):
    print('Message is caught')
    await message.forward(int(os.getenv('MY_CHANNEL')))

app.add_handler(MessageHandler(forward_client_messages, (filters.chat(target_chats) &
                                                         banned_words_filter & target_words_filter)))

if __name__ == '__main__':
    app.run()
