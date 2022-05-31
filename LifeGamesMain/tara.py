from Alone import AlphaIsAlone
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery, Message
from pyrogram import Client

# kiss trail omfoo...

@Client.on_message(filters.command("tara") & ~filters.via_bot & ~filters.group & ~filters.forwarded)
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
		
@Client.on_callback_query()
async def taraback(client: Client, query: CallbackQuery):
	user_id = query.from_user.id
	if target == user_id:
		if query.data == "tara":
			await query.message.edit_text(f"{message.reply_to_message.from_user.mention} accepted the kiss of {message.from_user.mention}...")
			
		elif query.data == "reject":
			await query.message.delete()
		
