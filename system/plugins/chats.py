
# Copyright (C) 2021 KeinShin@Github.






from sys import excepthook
from pyrogram.errors.exceptions.bad_request_400 import AdminRankInvalid, ChatAdminRequired
from pyrogram.errors.exceptions.forbidden_403 import RightForbidden, UserPrivacyRestricted
from pyrogram.types.messages_and_media.message import Message
from system.plugins import light

from system import DEVS, app, HNDLR
from pyrogram.errors import MediaCaptionTooLong

@light.on("get chats", grup=-1)
async def chat(client ,message):
    try:
        txt = message.text
        un = txt.split()[2]
    except IndexError:
        await message.edit(f"**Correct Syntax**: {HNDLR}get chats (user name) for more do {HNDLR}details chats")
    name = ""
    username = ""
    common = await  app.get_common_chats(un)
    a = ""
    pic = await app.get_profile_photos(un, limit=1)
    for i in pic:
        a += i['file_id']
    o = await app.download_media(a)
    
    for i in common:
       a = str(i['username'])
       name += f' - {a.replace("None", "**No Username**")}  '+ "\n"+ f'**Name** - `{i["title"]}`'  
    try: 
     await app.send_photo(message.chat.id, photo=o,caption= f"**{un}** is common in Groups\n {name}\n\{username}", force_document =False)
    except MediaCaptionTooLong:
     await message.edit("**Demn too common groups :/**")



@light.on(["user", 'whois', 'identify', "find"], grup=-1)
async def _(client, message):
    try:
        txt = message.text

        a = txt.split()[1]
    except IndexError:
        await message.edit(f"**Syntax**: {HNDLR}user or whois or identify or find user id/ name")
    user = await app.get_users(a)
    name = user.first_name
    is_fake = user.is_verified


    is_bot = user.is_bot

    contact = user.is_contact
    restric = user.is_restricted
    skam = user.is_scam
    status = user.status
    username = user.username
    photo = user.photo['small_file_id']
    p = await app.download_media(photo)
    await message.delete()
    await app.send_photo(message.chat.id, photo=p,caption=f"**Info about** __{username}__\
    \n\n**First Name**:- `{name}`\
    \n**__Fake__** - `{is_fake}`\
    \n**__Is Contact__**: `{contact}`\
    \n**__Is restricted  :- `{restric}`\
    \n\n**__Is Scam__**: `{skam}`\
    \n**__Last Online__**:- `{status}`\
    \n**__Is Bot__**: `{is_bot}`")


@light.on(['unban'])
async def s(client, message):
    txt = message.text
    if "all" in txt:
        s=0
        c=0
        await message.edit(f"**Unbanning every memeber of chat {message.chat.id}**")
        async for member in app.iter_chat_members(message.chat.id, filter="kicked"):
          try: 

            try:
              await app.unban_chat_member(
    chat_id=message.chat.id,
    user_id=member.user.id)
              s+=1
            except Exception:
               c += 1
            await message.edit(f"**Successfully unbanned {s} user failed for {c}**")
          except RightForbidden:
            await message.edit("**See me dont hab rights TwT**")
          except ChatAdminRequired:
            await message.edit("**Eh, not an admin**")

    else:
        try:

          await app.unban_chat_member(message.chat.id, txt.split()[1])
        except RightForbidden:
            await message.edit("**See me dont hab rights TwT**")
        except ChatAdminRequired:
            await message.edit("**Eh, not an admin**")
        await message.edit(f"**Unbanned user {txt.split()[1]}")

@light.on(['link'])
async def link(client, message):
    a = message.text
    try:

      if " " in a:
          a = message.split()[1]
          l=await app.export_chat_invite_link(a)
          await message.edit(f"**Chat link**\n\n{l}")
      else:
          l=await app.export_chat_invite_link(message.chat.id)
          await message.edit(f"**Chat link**\n\n{l}")
    except ChatAdminRequired:
        await message.edit("**Me ain't an admin**")


@light.on("id")
async def id(client ,message):
    txt = message.text
    a = message.reply_to_message
    if  a:
         sed =     await app.get_users(a.from_user.id)
         await message.edit(f"**ID** - `{sed.id}`")
    if " " in txt:
         sed =     await app.get_users(txt.split()[1])
         await message.edit(f"**ID** - `{sed.id}`")



@light.on(["invite"])
async def ins(client, message):
    txt = message.text
    chet = txt.split()[2]
    if "all" in txt:
        async for member in app.iter_chat_members(txt.split()[2]):
            user=member.user.id
            c= 0
            a = 0
            try:
      
                await app.add_chat_members(chet, user)
                a += 1
            except Exception:
              c += 1
            await message.edit(f"**Invited** - {a}\n**Failed** - {c}")
    else:
        chet = txt.split()[1]
        user = txt.split()[2]
        try:
            await app.add_chat_members(chet, user)
            await message.delete()
        except UserPrivacyRestricted:
            await message.edit("**Failed to invite due to user privacy**")
        except BaseException as e:
            await message.edit(f"ERROR - {e}")


@light.on("pin")
async def pin(client, message: Message):
    txt = message.text
    a = message.reply_to_message
    if a:
        try:  
         await app.pin_chat_message(message.chat.id, a.reply_to_message.message_id)
         await message.delete()
        except RightForbidden:
            await message.edit("**See me dont hab rights TwT**")
        except ChatAdminRequired:
            await message.edit("**Eh, not an admin**")



@light.on('unpin')
async def unpin(client , message: Message):
    txt = message.text
    a = message.reply_to_message
    if a:
        try:
          await   app.unpin_chat_message(message.chat.id, a.message_id)
          await message.delete()
        except ChatAdminRequired:
            await message.edit("**Eh, not an admin**")
    if "all" in txt:
        try:
            await app.unpin_all_chat_messages(message.chat.id)
            await message.edit("Upinned all message")
        except ChatAdminRequired:
            await message.edit("**Eh, not an admin**")
@light.on("promote")
async def s(client, message: Message):
    txt = message.text
    a = message.reply_to_message
    if a:
        
        await app.promote_chat_member(message.chat.id, a.from_user.id)
        await message.edit(f"Successfully promoted user {a.from_user.username}")
    
    if " " in txt:
        try:

         s = txt.split()[1]
        except IndexError:
            await message.edit(f"Syntax - __{HNDLR}promote <reply to user> or <provide username/id>__")
        try:
            await app.promote_chat_member(message.chat.id, s)
            await message.edit(f"Successfully promoted user {s}")
        except ChatAdminRequired:
            await message.edit("**Eh, not an admin**")
        except RightForbidden:
            await message.edit("**See me dont hab rights TwT**")


@light.on('kick')
async def kick(client, message: Message):
    txt = message.text
    a = message.reply_to_message
    if a:
        await app.kick_chat_member(message.chat.id, a.from_user.id)
        await message.edit(f"**WeW, {a.from_user.username} is out from the group")
    else:
        try:

         s = txt.split()[1]
        except IndexError:
            await message.edit(f"Syntax - __{HNDLR}kick <reply to user> or <provide username/id>__")
        await app.kick_chat_member(message.chat.id, s)
        await message.edit(f"**WeW, {s} is out from the group")

@light.on("create")
async def create(client, message: Message):
    txt = message.text
    try:

        s = txt.split()[2]
    except IndexError:
            await message.edit(f"Syntax - __{HNDLR} create group <name> | channel <name> <Description>__")
    if "group" in txt:
      try: 
       await app.create_group(s, (await app.get_me()).id)
       await message.edit(f"**Group created {s}**")

      except BaseException as e:
          await message.edit(e)
    if "channel" in txt:
     try:

        s3 = txt.split()[3]
     except IndexError:
            await message.edit(f"Syntax - __{HNDLR} create channel <name> <Description>__")
     try: 
       await app.create_channel(s, s3)
       await message.edit(f"**Channel created {s} with desc {s3}**")
     except BaseException as e:
          await message.edit(e)



@light.on('leave')
async def l(client, message):
    await message.edit("**See ya me iz leaving this chat**")
    await app.leave_chat(message.chat.id)

@light.on("gphoto")
async def semx(client, message: Message):
    a = message.reply_to_message
    if a:
        s= a.photo.file_id
        try:

         await app.set_chat_photo(message.chat, photo=a)
        except ChatAdminRequired:
            await message.edit("**Eh, not an admin**")
        except RightForbidden:
            await message.edit("**See me dont hab rights TwT**")
    else:
        await message.edit("**Reply to a pic**")

