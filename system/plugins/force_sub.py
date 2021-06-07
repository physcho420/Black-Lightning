
 # Copyright (C) 2021 KeinShin@Github. All rights reserved



from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from system.plugins import light
from system import COMMAND_HELP, HNDLR, app, bot
from pyrogram import filters
from system.datas_sqlite.chat_sqllite import (
   CreateSafeUser,
   insert_chet,
   Allchats,
   chet,
   get_safe_user,
   d as chat,
   c,
   chats,
   safe_users

)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions, CallbackQuery, Message



channel = []
channel_ = {}


def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None



@light.on(["forcesub"])
async def force(client, message):
    
    try:
     txt = message.text.split()[1]
     name = message.text.split()[2]
    except IndexError:
        await message.edit(f"**Correct Syntax**: `{HNDLR}forcesub (channel user name) ( group user name )`")
    for i in chet(username=name):
        for s in i:
         channel.append(s)
    try:
        await message.edit(f"**Force Subscribe enable** for channel {txt} in group {name}\n\n© [Black Lightning](https://github.com/KeinShin/Black-Lightning)")
        insert_chet(name , txt)
    except BaseException as e:
        await message.edit(f"**ERROR** - {e}")


@bot.on_message(filters.chat(
    chats
) & ~filters.via_bot)
async def sub(client, message: Message):
    m = message.chat.username
    sm=  f"@{m}"
    aaia = message.from_user['id']
 
  
    if message.from_user.username or aaia in safe_users:
        return
    try:
     keys = sum(any(sm in s for s in subList) for subList in chat.values())

     await bot.get_chat_member(chat[sm], message.from_user.id)
    except UserNotParticipant:
        await bot.restrict_chat_member(message.chat.id, aaia, ChatPermissions(can_send_messages=False))

        mkp = InlineKeyboardMarkup(
                [[InlineKeyboardButton("Unmute", callback_data="chata")],
                [InlineKeyboardButton("Channel", url=f"t.me/{chat[sm].replace('@', '')}")],
                [InlineKeyboardButton("Dis-Card ( only admin )", callback_data="unmute_{}".format(message.from_user.id))]
                ]
            )
        await bot.send_message(message.chat.id, "[{}]({}), You havent subscribe our channel [{}]({}). Go and Subscribe Now! then press un-mute\n\n[Featured By Black Lightning](https://github.com/KeinShin/Black-Lightning)".format(message.chat.first_name, f'tg://user?id={message.chat.id}',chat[sm],aaia ), reply_markup=mkp)
     

@bot.on_callback_query(filters.regex(pattern="chata"))

async def detailed(client, chet: CallbackQuery):
    sed=chet.message.chat.username

    s=await app.get_chat_members(sed, filter="administrators") 
    admin = ""
    for i in s:
        a = i['user']
        admin+= "\n"+ str(a['username'])
    user =  await  app.get_chat_member(sed, chet.from_user.username)

    if chet.from_user.username in admin:
        text= "You are admin lol, No can mute you except Owner OwO"
        await client.answer_callback_query(
    chet.id,
    text=text,
    show_alert=True
)       
        return

    elif user.user.is_restricted:
        text = "Bruh, u r mute by someone else not by me :/"
        await client.answer_callback_query(
    chet.id,
    text=text,
    show_alert=True
)       
        return
    else:

        m = chet.from_user['id']
        d=chet.message.chat.username
        d=f"@{d}"
        # chn = {}
        try:
        #  c.execute("SELECT * FROM chats")     
        #  s=c.fetchall()
        #  for i in s:
        #     chn.update({
        #     f"{i[0]}": f"{i[1]}"
        # })
         await app.get_chat_member(chat[d], chet.from_user.username)
         await bot.restrict_chat_member(chet.message.chat.id, chet.from_user.username, ChatPermissions(can_send_messages=True))
         await chet.message.delete()
        except UserNotParticipant:
    
         user =  await  app.get_chat_member(d, chet.from_user.username)
         text = "You haven't subscribed channel yet!"

         await client.answer_callback_query(
        chet.id,
        text=text,
        show_alert=True
)


@bot.on_callback_query(filters.regex(pattern="unmute_(.*)"))

async def s(client, chet: CallbackQuery):
    sed=chet.message.chat.id
    user_ = chet.matches[0].group(1)
 
    s=await app.get_chat_members(sed, filter="administrators") 
    admin = ""
    for i in s:
        a = i['user']
        admin +=  str(a['username'])
    user =  await  app.get_chat_member(sed, chet.from_user.username)

    if not chet.from_user.username in admin:
        text =  "Sed, You aren't an admin XoX"
        await client.answer_callback_query(
    chet.id,
    text=text,
    show_alert=True
)       
        return
    else:
      CreateSafeUser(user_)
  
      await bot.restrict_chat_member(chet.message.chat.id, user_, ChatPermissions(can_send_messages=True))
      await bot.send_message(chet.id, text=f"**User Unmuted by admin {chet.from_user.username}**")

COMMAND_HELP.update({
    "force_sub": f"`{HNDLR}forcesub` **(channel) (group)**",
    "force_sub's help": "**Use**: `Force Subscribe the channel in that particular group via your assistant`\
    \n**Note**: `First add assistant to that channel as admin and similary add assistant in that group with admins rights` ( add admins is not mandatory )"
})
