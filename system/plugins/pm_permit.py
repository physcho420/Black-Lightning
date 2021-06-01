 # Copyright (C) 2021 KeinShin@Github. All rights reserved
from system.plugins.inline import Friends, USER
import pandas as pd
from pyrogram.types.messages_and_media.message import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from system.Config.utils import hd_no, language
import re
from pyrogram import filters

from system import  *
from collections import OrderedDict
from system.decorators import owner
from collections import Counter
from system.plugins import light

from system.datas_sqlite.pm_sqlite import (
    approve,
    approved,
    disapprove,
    all_user,
    disapprove ,
    his_turn,
    update_turns,
    turn,
    remove_user

)
SPAMMERS = []
LIMIT = []
SPAM_LIMIT = []


""""""



def counter(func):
      def wrapper():
       wrapper.count += 1
    # Call the function being decorated and return the result
       return func()
      wrapper.count = 0
  # Return the new decorated function
      return wrapper

DEVS = "1311769691" # more to be added


        


@light.on(["a","ap", "approve"])
async def ap(client, message: Message):
       users=list(OrderedDict.fromkeys(all_user()))
       if Variable.PROTECTION == "OFF":
          logging.info("Execution Failed as Protection is off")
          return   
       try:

        #   await message.edit(f"**{language('APPROVED! USER')} USER** - {id}")
        #   approve(id)
          if  message.reply_to_message:
            await message.edit(f"**{language('APPROVED! USER')} USER** - {message.reply_to_message.from_user.id}")
            approve(message.reply_to_message.from_user.id)
            await message.delete()

          elif " " not in  message.text:
            await message.edit(f"**{language('APPROVED! USER')} USER** - {message.chat.id}")
            approve(message.chat.id)
            await asyncio.sleep(1)
            await message.delete()

          else:
            name = message.text.split()[1]
            await message.edit(f"**{language('APPROVED! USER')}** - NAME {name}")
       
            approve(name)
            await asyncio.sleep(1)
            await message.delete()

       except BaseException as e:
            await message.edit(e)






@light.on(["da", "disap", "disapprove"])
async def dis(client, message: Message):
    if Variable.PROTECTION == "OFF":
          logging.info("Execution Failed as Protection is off")
          return   
    users=list(OrderedDict.fromkeys(all_user()))

    if " " not in message.text:


      await message.edit(f"{language('DISAPPROVED USER - ')} {message.chat.id}")

      disapprove(message.chat.id)
      users.remove(f'{message.chat.id}')
      await message.delete()
    elif      message.reply_to_message:
      users=list(OrderedDict.fromkeys(all_user()))
    
      await message.edit(f"**{language('DISAPPROVED USER - ')}** - {message.reply_to_message.from_user.first_name}")

      disapprove(message.reply_to_message.from_user.id)
      users.remove(f'{message.chat.id}')
      await message.delete()

    elif " " in message.text:
      users=list(OrderedDict.fromkeys(all_user()))

      name = message.text.split()[1]
      await message.edit(f"**{language('DISAPPROVED USER - ')}** - {name}")
      users.remove(f'{message.chat.id}')
      disapprove(message.chat.id)
      await message.delete()


@counter
@app.on_message(filters.private & ~filters.edited & ~filters.me & ~filters.bot)
async def pm(client, message: Message):
    if Variable.PROTECTION == "OFF":
      return   
    users=list(OrderedDict.fromkeys(all_user()))
          
    sed = False
    try:

    
     sed=turn(message.chat.id)[PM_LIMIT]
     sed = True  if sed else False
    except KeyError:
     pass
    mister = await app.get_users(int(message.chat.id))
    pro = ""
    for i in users:
       pro += ","+ " " + f"{i}"

    if not str(message.chat.id) in pro :
        update_turns(message.chat.id)
        if PM_PERMIT.endswith(".mp4") and not str(message.chat.id) in pro:
          await app.delete_messages(message.chat.id, message.message_id, revoke=True) 
          await app.send_video(message.chat.id, PM_PERMIT)
          bot_results =  await app.get_inline_bot_results("Kakrotooobot", "Pm Protect")
          update_turns(message.chat.id)

          await  app.send_inline_bot_result(
    message.chat.id,
    bot_results.query_id,
    bot_results.results[0].id)


        elif PM_PERMIT.endswith(".png") or PM_PERMIT.endswith(".jpg") and not str(message.chat.id) in pro:
          update_turns(message.chat.id)

          await app.send_photo(message.chat.id, PM_PERMIT,)
          bot_results=await app.get_inline_bot_results(g, "Pm Protect")
          await  app.send_inline_bot_result(
    message.chat.id,
    bot_results.query_id,
    bot_results.results[0].id
)
        
          
        elif sed and not str(message.chat.id) in pro:
            await app.send_message(message.chat.id, f"__I warned you {PM_LIMIT} times now its time for action byy__\n\n**BLOCKED**")
            await app.block_user(message.chat.id)

   # sed=list(OrderedDict.fromkeys(sed))

    if mister.is_bot:
        return
    if mister.is_contact:
        return
    if mister.is_mutual_contact:

    
        return
    if str(mister.id) in  DEVS and not  str(mister.id) in users:
        await app.send_message(message.chat.id, "**Dev Detected in pm, approved**")
        approve(mister.id)
        return
    if mister.is_scam:
        alt = language('ALERT')
        scm = language('SCAMMER')
        await bot.send_message(chet, f"__{alt}__!\n**{scm} [{mister.first_name}]({mister.id}) IN PM**")
        await app.send_message(message.chat.id, f"{language('Scammer Alert! Therefore blocked and informed master!')}")
        await app.block_user(message.chat.id)
        return
    if DELETE_MSG == "on":
        
        await app.delete_messages(message.chat.id, message.message_id, revoke=True)
        return
    # if message.chat.is_fake:
    #     await app.send_message(message.chat.id, f"**{language('FAKE ID ALERT')}!--")

    #     return

    if   message.chat.id in users:
       logging.info("USER PASSES")
    

      


def user_abused(txt):
    # sed=predict_prob([txt])
    # if sed > 0.5:
    #     return True
    # else:
    #     return False

    # return None
    pass


@light.on(["listapprovd"])
async def liast(client, message):
    users=list(OrderedDict.fromkeys(all_user()))
   
    noice=users
    await app.send_message(message.chat.id, f"**{language('USERS - APPROVED')}**\n\n__{noice}__")


 
# def approve(id, turn):

COMMAND_HELP.update({
    "pm_permit": f"`{HNDLR}approve or a `\
    \n`{HNDLR}da or disapprove`\
    \n`{HNDLR}listapprovd`",
    "pm_permit's help": f"`{HNDLR}approve or a `\
    \n**USE**: __Approves user to your pm means he or she can pm you!__\
    \n\n`{HNDLR}da or dispprove\
    \n**USE**: __Disapproves user from your pm!__ `\
    \n\n{HNDLR}listapprovd\
    \n**USE**: __approves user to your pm__",
    "pm_permit's type": "Security"
})
