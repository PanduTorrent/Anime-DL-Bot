# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Totally Optional

def instructions(client, callback_query):
    query = callback_query
    query.answer("Please Read Carefully!!!")
    keyb = [
        [InlineKeyboardButton("Search Anime Inline", switch_inline_query_current_chat="")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    query.edit_message_caption(caption="""**This Bot can Get your favourite Anime and It provides Download Link with a fastest server(Google drive).**

**Points to Be Noted :-**

__👉For streaming in mobile, open the links with VLC Media Player. You can also use MX Player.__

__👉For streaming in PC, use VLC media player network stream.__

__👉For downloads, just open the links in a browser.__

**That's it, ENJOY BITCHES 😁✌**

**BOT MADE BY @pie_yush. For personal use only. If source used without permission, INSTANT BAN**

**Type /search to Search for an Anime...**""", parse_mode="markdown", reply_markup=reply_markup)
