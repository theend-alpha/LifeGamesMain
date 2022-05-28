from Alone import AlphaIsAlone
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message, CallbackQuery

@Client.on_message(filters.group & ~filters.edited & ~filters.forwarded & ~filters.via_bot & filters.command("tara"))
async def start(bot, message: Message):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
		message.chat.id,
		AlphaIsAlone.TARA.format(msg.from_user.mention, message.reply_to_message.from_user.mention),
                disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(AlphaIsAlone.tara_buttons)
	)

target_id = message.reply_to_message.from_user.id

@Client.on_callback_query(filters.regex("reject"))
async def rej(bot, query: CallbackQuery):
    await query.message.delete()

@Client.on_callback_query(filters.regex("tara"))
async def acc(bot, query: CallbackQuery):
    if query.from_user.id == target_id:
        await query.message.reply_photo(alpha,
            caption=AlphaIsAlone.TARAA.format(message.reply_to_message.from_user.id, message.from_user.id))    

    else:
        await query.answer("This is not for you !")
