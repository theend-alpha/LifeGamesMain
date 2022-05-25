from Alone import AlphaIsAlone
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message, CallbackQuery

@Client.on_message(filters.group & ~filters.edited & ~filters.forwarded & ~filters.via_bot & filters.command("tara"))
async def start(bot, msg: Message):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
		msg.chat.id,
		AlphaIsAlone.TARA.format(msg.from_user.mention, message.reply_to_message.from_user.mention),
                disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(AlphaIsAlone.tara_buttons)
	)

@Client.on_callback_query(filters.regex("reject"))
async def rej(bot, query: CallbackQuery):
    await query.msg.delete()

