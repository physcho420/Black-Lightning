from system.plugins import light

from system.datas_sqlite.echo_sqlite import *

from pyrogram import filters
from system import app

@light.on(['echo', "rmecho"])
async def s(client, message):
    a= message.reply_to_message
    ah = a.from_user.username
    at  = message.text
    if a:
        if ah is None:
          insert_user(a.from_user.id ,int_= True)
        else:
          insert_user(ah)  
        await message.edit(f"**Echo Enabled for user @{a.from_user.username}**")

    else:
        await message.edit("**Reply to the user**")
        


@app.on_message((filters.text | filters.document | filters.photo | filters.sticker | filters.animation| filters.video | filters.media) & filters.user(user))
async def echo(client, message):
    if message.sticker:
       await message.reply_sticker(message.sticker.file_id)
    elif message.animation:
        await message.reply_animation(message.animation.file_id)
    elif message.text:
         await message.reply_text(message.text)