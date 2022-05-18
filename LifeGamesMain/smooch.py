from telethon import events, version, Button
from telethon.tl.custom import button
from LifeGamesMain import ALF
from telethon.tl.functions.users import GetFullUserRequest

@ALF.on(events.NewMessage(incoming=True, pattern="/smooch")
async def smooch(event):


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
