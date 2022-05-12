from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from Yashvi import Keshav


# Start Message
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
