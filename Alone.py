from pyrogram.types import InlineKeyboardButton


class AlphaIsAlone:

    #smooch msg
    SMOOCH = """

💗{} wants to smooch {}...

"""

    #smooch buttons
    smooch_buttons = [ 
          [  
          InlineKeyboardButton(" ✅ ", callback_data="smooch"),
          InlineKeyboardButton(" ❌ ", callback_data="reject")
          ]
    ]

    #smooch accept
    SMOOCHA = """

{} accepted the kiss of {} .

"""
