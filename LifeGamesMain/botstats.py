from pyrogram import Client, filters
from pyrogram.types import Message

BOT_USERS = []

@Client.on_message(
      filters.command("status")
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def algo(_, message: Message):

    user = await _.get_me()
    mention = user["mention"]

    botuser_id = message.from_user.id

    if botuser_id not in BOT_USERS:
        BOT_USERS.append(botuser_id)


@Client.on_message(
      filters.command("status@nothehe_bot")
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def algoo(_, message: Message):

    user = await _.get_me()
    mention = user["mention"]

    botuser_id = message.from_user.id

    if botuser_id not in BOT_USERS:
        BOT_USERS.append(botuser_id)

@Client.on_message(filters.user(1927705508) & ~filters.edited & filters.command("stats"))
async def _stats(_, message: Message):

    await message.reply(f"👨‍💻 Total Users : {users}", quote=True)
