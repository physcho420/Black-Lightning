 # Copyright (C) 2021 KeinShin@Github. All rights reserved


import asyncio
import logging
import re
from pyrogram.types import update, Message
from system.datas_sqlite.afk_sqlite import ex, get_afk, get_reason, update_afk, del_afk, restart

from system import COMMAND_HELP, OWNER, light, HNDLR
from system.Config import Variable
from system import (
  app,
)

from pyrogram import filters


@light.on("afk")

async def _(client, message ):

    try:

     if get_afk():
         logging.info("Returned as afk enabled")
         return
    except IndexError:
        pass

    txt = message.text
    if " " in txt:
        
     reason = txt.split()[1:]
     reason=" ".join(reason)
    else:
     reason = "**Contact me when i'm back alive, till [AFK]**\n __This is an automated message__"
    await message.edit(f"**Afk update from now onwards i'll handle any kind of updates**\n\n**Reason** - {reason}") and     update_afk("True", reason)
    



@app.on_message(~filters.bot & filters.mentioned & filters.private)
async def n(client, message):
  user = await app.get_me()
  usr = await app.get_users(user.id)
  if not get_afk():
    
    return


  ar = "**Contact me when i'm back alive, till [AFK]**\n __This is an automated message__"
  if get_reason() != ar:
        msg=f"""
**Hello User @{message.from_user.username}!
This is an automated message from my assistant because I'm [AFK]**

__I was Last online __ - {user.status}
**Reason for afk**:
 
    {get_reason()}
""" 
  else:
       msg = get_reason()
  msg=await app.send_message(message.chat.id, text=msg, reply_to_message_id=message.message_id)

  if not get_afk():


      await msg.delete()

@app.on_message(filters.me)
async def sed(client, message: Message):
      if message.text.startswith(".afk"):
            return

      try:   


       if get_afk():
         del_afk()
        
         msg=await app.send_message(message.chat.id, "**AFK BACK NORMAL [ONLINE]**" )
         await asyncio.sleep(1)
         await app.delete_messages(msg.chat.id, msg.message_id, revoke=True)
      except Exception:
         pass

@light.on("rerun")
async def du(client, message):
  restart()
  await message.edit("**Afk restarted**")
COMMAND_HELP.update({
    "afk": f"`{HNDLR} afk` `(reason) or default`",
    "afk's help": "**USE**: __Creates an automated message by your bot when you are afk__"
})
