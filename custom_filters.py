import re

from pyrogram import filters
from pyrogram.types import Message


def banned_words_filter(words: list):
    async def func(_, __, message: Message):
        # Проверяем, есть ли текст в сообщении
        if not message.text:
            return False

        # Создаем шаблон из запрещенных слов
        pattern = '|'.join(map(re.escape, words))

        # Проверяем наличие запрещенных слов
        if re.search(pattern, message.text, re.IGNORECASE):
            return False
        return True

    # Создаем и возвращаем фильтр
    return filters.create(func)


def target_words_filter(words: list):
    async def func(_, __, message: Message):
        # Проверяем, есть ли текст в сообщении
        if not message.text:
            return False

        # Создаем шаблон из нужных слов
        pattern = '|'.join(map(re.escape, words))

        # Проверяем наличие нужных слов
        if re.search(pattern, message.text, re.IGNORECASE):
            return True
        return False

    # Создаем и возвращаем фильтр
    return filters.create(func)
