 # Copyright (C) 2021 KeinShin@Github. All rights reserved


import logging
from pyrogram.types.messages_and_media.message import Message
from system.datas_sqlite.filters_sqlite import delete, insert, filters, chats, cmds
from pyrogram import filters as ft
from collections import OrderedDict


from system import app
from system.plugins import light


@light.on(["filter", "clear"])
async def s(client, message):
    txt = message.text
    chet = message.chat.username
    filter_ = txt.split()[1]
    if chet is None:
          chet  = str(message.chat.id)
    if "filter" in txt:
      text = txt.split()[2:]
      text=",".join(text)
      await message.edit(f"**Filter updated of {text} get it with {filter_}**")
  
      insert(chet, filter_, text)
    elif "clear" in txt:
        try:

         delete(chet, filter_)
        except BaseException as e:
            await message.edit(f"**Failed to remove**\n\n**ERROR** - `{e}`")
        await message.edit(f"{filter_} **Removed successfully**")
insert(-1001269074519, "Hlo", "Hi")
sed =  filters()

sed = sed['-1001269074519'+ '_Hlo']

print(sed)
@app.on_message(ft.chat(chats()))
async def h(client, message: Message):
    msg = message.message_id
    chet= str(message.chat.username)
    if chet is None:
      chet  = str(message.chat.id)
    #   logging.info("Filter Not Excecuted as  a private chat")
    sed = filters()
    txt = message.text
    if txt in cmds():
        try:
       
         await app.send_message(message.chat.id, sed[chet+ "_" + txt], reply_to_message_id=msg)
        except IndexError:
            pass
        except KeyError:
            pass
