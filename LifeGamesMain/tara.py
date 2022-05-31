from Alone import AlphaIsAlone
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery, Message
from pyrogram import Client, filters

# kiss trail omfoo...

@Client.on_message(filters.command("tara") & ~filters.via_bot & filters.group & ~filters.forwarded)
async def tara(_, message: Message):
	chat_id = message.chat.id
	global omfoo
	try:
		omfoo = message.from_user.id
	except:
		return
	global target
	try:
		target = message.reply_to_message.from_user.id
	except:
		return
	try:
	    await _.send_message(message.chat.id,
		AlphaIsAlone.TARA.format(message.from_user.mention, message.reply_to_message.from_user.mention),
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(AlphaIsAlone.tara_buttons))
	except:
		return
	
		
@Client.on_callback_query()
async def taraback(_: Client, query: CallbackQuery):
	user_id = query.from_user.id
	if query.data == "tara":
		if user_id == target:
			await query.message.reply_photo(alpha,
			caption= f"{message.reply_to_message.from_user.mention} accepted the kiss of {message.from_user.mention}...")
			await query.message.delete()
			
		else:
			await query.answer("this is not for you !")
			
	elif query.data == "reject":
		if user_id == target:
			await query.message.delete()
			
		else:
			return
