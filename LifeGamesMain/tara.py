from Alone import AlphaIsAlone
from pyrogram import Client, Message
from pyrogram.types import InlineKeyboardMarkup, filters

@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
		msg.chat.id,
		Data.START.format(msg.from_user.mention, mention),
                disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(Keshav.alpha_buttons)
	)
