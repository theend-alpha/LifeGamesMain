from Data import Data
from Yashvi import Keshav
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from Alone import AlphaIsAlone
from LifeGamesMain.smooch import TARGET_ID

smooch = "https://te.legra.ph/file/2bd00c6b47f9f3a7bfe1d.jpg"

@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user["mention"]
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.message_id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Keshav.alpha_buttons),
            )
    elif query == "credits":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Keshav.CREDITS,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Keshav.home_button),
        )
    elif query == "cmda":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Keshav.CMDA,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Keshav.home_button),
        )
    elif query == "smooch":
        chat_id = callback_query.from_user.id 
        message_id = callback_query.message.message_id
        if chat_id in TARGET_ID:
            await callback_query.message.reply_photo(smooch,
                caption=AlphaIsAlone.SMOOCHA)
            await bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=message_id,
                    text="accepted !")
    elif query == "reject":
        chat_id = callback_query.from_user.id 
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="accepted !")
    
