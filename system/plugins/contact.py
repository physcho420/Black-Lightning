# Copyright (C) 2021 KeinShin@Github.

from pyrogram.raw.functions.contacts import AddContact

from system.Config.utils import language
from system import (

  app,
  g,
  bot,
  a,
  HNDLR,
  COMMAND_HELP

)
from system import light

@light.on(["send contact"])
async def contact(client, message):
    # no  = message.text.split(" ")[2]
    name = message.text.split(" ")[2]
    message.delete()
    # if not no and name:
        # syntx=language("Syntax")
        # await message.edit(f"{syntx}: {HNDLR}send contact (phone number) (name)")
        # return
    await app.send_contact(message.chat.id, first_name =name, disable_notification=True)



@light.on(["add contact"])
async def apsp(client, message):
    o = message.text.split()[2]
    o1 = message.text.split()[3]
    try: 
       await app.add_contacts(o, o1)
       await app.send_message(message.chat.id , f"**CONTACT ADDED with name {o1} and no {o[0:4]}XXXX XXXXXX**", reply_to_message_id=message.message_id)
    except BaseException as e:
        await app.send_message(message.chat.id, e)
    
    await message.delete()

@light.on(["del contact"])
async def apap(client, message):
    o = message.text.split()[2]
    if message.text.split()>1:
        sed=message.text.split()
        await app.delete_contacts(sed)
        peru =""
        count = 0
        for i in sed:
            peru += "\n" + i
            count += 1
        await app.send_message(message.chat.id , f"**{count} CONTACT's REMOVED from  with name or ids\n {peru}", reply_to_message_id=message.message_id)

    try: 
       await app.delete_contacts(o)
       await app.send_message(message.chat.id , f"**CONTACT REMOVED with name {o}", reply_to_message_id=message.message_id)
    except BaseException as e:
        await app.send_message(message.chat.id, e)
    
    await message.delete()







g=language('Gets the given contact')
COMMAND_HELP.update({
    "contact": f"`{HNDLR}send contact` `(phone no.) (name)`\
    \n`del contact` `(id / name)`\
    \n`{HNDLR}add contact` `(number) (name for the given contact)`",
    "contact's help": f"**USE**: __{g}__\
    \n\n`{HNDLR}del contact` (id / name)\
    \n**USE**: __{language('REMOVES CONTACT')}__!\
    \n\n`{HNDLR}add contact` (number) (name for the given contact)\
    \n**USE**: {language('ADDs user to your contact.')}"
})