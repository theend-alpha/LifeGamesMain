from telethon import events, version, Button
from telethon.tl.custom import button
from LifeGamesMain import ALF
from telethon.tl.functions.users import GetFullUserRequest

@ALF.on(events.NewMessage(incoming=True, pattern="/smooch")
async def smooch(event):
