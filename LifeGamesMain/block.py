from pyrogram import Client, filters
from pyrogram.types import Message

OWNER_ID = [1927705508]

V_ID = []

@Client.on_message(
      filters.user(1927705508)
    & filters.command("addv")
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def addv(_, message: Message):
        user = await _.get_me()
        target_id = message.reply_to_message.from_user.id
        alpha = await message.reply("""Adding...!""")

        if target_id not in V_ID:
        V_ID.append(target_id)

        await message.reply(f"Verified {}".format(target_id))
        await alpha.delete()
