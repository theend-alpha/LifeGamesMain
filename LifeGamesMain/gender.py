from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from Yashvi import Keshav

@Client.on_message(
      filters.command("gender")
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def gender(_, message: Message):
        await message.reply("start bot --> settings --> gender ",
                            reply_markup=InlineKeyboardMarkup(Keshav.gender_button))


@Client.on_message(
      filters.command("gender@nothehe_bot")
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def gendero(_, message: Message):
        await message.reply("start bot --> settings --> gender ",
                            reply_markup=InlineKeyboardMarkup(Keshav.gender_button))
