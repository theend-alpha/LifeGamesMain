from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

@Client.on_message(
      filters.command("gender")
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def gender(_, message: Message):
        await message.reply("Click [here](t.me/nothehe_bot) to change gender",
                            disable_web_page_preview=True)
