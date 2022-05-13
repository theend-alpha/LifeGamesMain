from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from Yashvi import Keshav

@Client.on_message(
      filters.command("algorithm")
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def gender(_, message: Message):
        await message.reply(Keshav.ALGO,
                            reply_markup=InlineKeyboardMarkup(Keshav.hexa_button))


@Client.on_message(
      filters.command("algorithm@nothehe_bot")
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def gendero(_, message: Message):
        await message.reply(Keshav.ALGO,
                            reply_markup=InlineKeyboardMarkup(Keshav.hexa_button))
