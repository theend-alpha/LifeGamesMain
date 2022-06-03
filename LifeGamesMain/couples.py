from LifeGamesMain.AlphaDB.shipdb import get_couple, save_couple
from pyrogram import filters, Client
import random
from datetime import datetime as dt 


a = dt.now()

if a.minute >= 30 and a.hour < 18:
	k = a.minute

	atime = str(a.hour + 6) + ":" + str(k - 30)


elif a.minute >= 30 and a.hour >= 18:
	k = a.minute
	t = a.hour
	
	atime = str(t - 18) + ":" + str(k - 30)
	
	
elif a.minute < 30 and a.hour < 19:
	k = a.minute
	t = a.hour
	
	atime = str(t + 5) + ":" + str(k + 30)

	
elif a.minute < 30 and a.hour >= 19:
	k = a.minute
	t = a.hour
	
	atime = str(t + 5 - 24) + ":" + str(k + 30)

@Client.on_message(filters.command("couple") & ~filters.edited)
async def couple(_, message):
    if message.chat.type == "private":
        await message.reply_text("This command only works in groups.")
        return
    try:
        chat_id = message.chat.id
        is_selected = await get_couple(chat_id, today)
        if not is_selected:
            list_of_users = []
            for i in _.iter_chat_members(message.chat.id):
                if not i.user.is_bot:
                    list_of_users.append(i.user.id)
            if len(list_of_users) < 2:
                await message.reply_text("Not enough users")
                return
            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c1_id = random.choice(list_of_users)
            c1_mention = (await _.get_users(c1_id)).mention
            c2_mention = (await _.get_users(c2_id)).mention

            couple_selection_message = f"""**Couple of the day:**
{c1_mention} + {c2_mention} = ❤️
__New couple of the day may be chosen at 12AM {tomorrow}__"""
            await _.send_message(message.chat.id, text=couple_selection_message)
            couple = {"c1_id": c1_id, "c2_id": c2_id}
            await save_couple(chat_id, today, couple)

        elif is_selected:
            c1_id = int(is_selected["c1_id"])
            c2_id = int(is_selected["c2_id"])
            c1_name = (await _.get_users(c1_id)).first_name
            c2_name = (await _.get_users(c2_id)).first_name
            couple_selection_message = f"""Couple of the day:
[{c1_name}](tg://openmessage?user_id={c1_id}) + [{c2_name}](tg://openmessage?user_id={c2_id}) = ❤️
__New couple of the day may be chosen at 12AM {tomorrow}__"""
            await _.send_message(message.chat.id, text=couple_selection_message)
    except Exception as e:
        print(e)
        await message.reply_text(e)
