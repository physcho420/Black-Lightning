

# Copyright (C) 2021 KeinShin@Github.
from pyrogram.errors import FloodWait
from system import COMMAND_HELP, app, HNDLR, DEVS
from . import light
from pyrogram.types import Message
@light.on('pic')
async def pic(client, message):
   txt=message.text
   if " " in txt:
       limit = txt.split()[1]
   else:
       limit = 1
   await message.edit("Processing")
   if int(limit)>1:
        await message.edit(f"**Getting Profile Pics with limit {limit}**")

        a=await app.get_profile_photos(message.reply_to_message.from_user.username, limit=limit)
        for i in a:

            a =await app.download_media(i.file_id)
            await  app.send_photo(message.chat.id,a)
   else:
        await message.edit(f"**Getting {await app.get_profile_photos_count(message.reply_to_message.from_user.username)} Profile Pics of {message.reply_to_message.from_user.username}**")

        if message.reply_to_message:
    
          async for photo in app.iter_profile_photos(message.reply_to_message.from_user.id):
             a =await app.download_media(photo.file_id)
             await  app.send_photo(message.chat.id,a)
        else:
           tx2=txt.split()[1]

           async for photo in app.iter_profile_photos(tx2):
                 a =await app.download_media(photo.file_id)
                 await  app.send_photo(message.chat.id,a)




@light.on(['set'])
async def pic(client, message):
    txt = message.text
    a =  message.reply_to_message
    if "bio" in txt:
        if a:

            await app.update_profile( bio=a.text)
        else:
            await app.update_profile( bio=txt.split()[1])
        await message.edit("**Bio updated**")
 
    elif "name" in txt:
        if a:
    
            await app.update_profile(first_name=a.text)
        else:
            await app.update_profile(first_name=txt.split()[2])  
        await message.edit("**Name updated**")

    txt = message.text
    if "uname" in txt:
     if message.reply_to_message:
         await app.update_username( message.reply_to_message.text)

     else:
        try:
         txt=txt.split()[1]
        except IndexError:
         await message.edit(f"**Syntax** : __{HNDLR}uname <name>__")
        await app.update_username(txt)
     await message.edit("**Username updates**")



@light.on('clone')
async def horny(client, message: Message):
    
    a = message.reply_to_message
    ab=a
    if str(a.from_user.id) in DEVS:
        await message.edit("**Sed can not clone the dev**")
        return
    user = await app.get_users(a.from_user.id)
    if a:
     try:
        await app.update_profile( first_name=user.first_name, last_name=user.last_name)
        a=await app.get_profile_photos(message.reply_to_message.from_user.username)
        try:

       
         a=a[0]
        except IndexError:
            pass
        a=await app.download_media(a.file_id)
        


        await app.set_profile_photo(a)
        await app.send_message("**Sed, Alien Spotted can change shape**", reply_to_message_id=ab.message_id)
        await message.delete()
     except FloodWait as e:
         await message.edit(f"**Flood wait for {e.x} is needed**")
COMMAND_HELP.update({
    "profile": f"`{HNDLR} pic <limit (if any)> | rply to user give input` | {HNDLR}clone <reply_to_user>\
    \n`{HNDLR}set name or uname or bio",
    "profile's help": f"**USE** - __`{HNDLR}pic` gets the profile pic of the user__ | __`{HNDLR}) set name` -- <change your profile pic>__\
    \n__`{HNDLR}set uname` <sets your own username>__\
    \n__{HNDLR}set bio <sets your own bio> \
    \n__{HNDLR}clone <clones everything of the user>__",
})