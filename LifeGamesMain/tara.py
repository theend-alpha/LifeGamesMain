from Alone import AlphaIsAlone
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, CallbackQuery

@Client.on_message(filters.command("tara") & filters.group & ~filters.forwarded & ~filters.via_bot)
async def tara(_, message: Message):
    global f_id
    global i_m
    global f_m
    i_id = message.from_user.id
    f_id = message.reply_to_message.from_user.id
    i_m = (await _.get_users(i_id)).mention
    f_m = (await _.get_users(j_id)).mention
    try:
        await _.send_message(message.chat.id,
                             AlphaIsAlone.TARA.format(i_m, f_m),
                             reply_markup=InlineKeyboardMarkup(AlphaIsAlone.tara_buttons))
    except Exception as e:
        await message.reply_text(f"Error : {e}")

@Client.on_callback_query()
async def taraback(_: Client, query: CallbackQuery):
    resp_id = query.from_user.id
    if resp_id == f_id:
        if query.data == "tara":
            
        
