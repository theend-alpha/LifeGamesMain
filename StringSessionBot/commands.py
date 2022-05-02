from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


@Client.on_message(filters.private & filters.incoming & filters.command("commands"))
async def _commands(bot, msg):
    await bot.send_message(
        msg.chat.id,
        Data.COMMANDS,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )