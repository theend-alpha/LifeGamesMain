from pyrogram import Client, filters 
from pyrogram.types import Message

@Client.on_message(filters.command("cousin") & filters.group & ~filters.forwarded & ~filters.via_bot)
async def cousin(_, message: Message):
    user = await _.get_me()
    mention = user["mention"]

    COUSINS_ID = []

    target_id = message.reply_to_message.from_user.id

    if target_id not in COUSINS_ID:
        COUSINS_ID.append(target_id)
    hehe = COUSINS_ID


@Client.on_meesage(filters.command("mystatus") & filters.group & ~filters.forwarded & ~filters.via_bot)
async def status(_, message: Message):
    user = await _.get_me()
    mention = user["mention"]
    await _.send_message(message.chat.id,
                         f"Cousins of {} are {}".format(message.from_user.mention, hehe))

