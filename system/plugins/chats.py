from pyrogram.errors.exceptions.bad_request_400 import AdminRankInvalid
from pyrogram.errors.exceptions.forbidden_403 import RightForbidden
from system.plugins import light

from system import app, HNDLR
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


@light.on(['unban'], grup=-1)
async def s(client, message):
    txt = message.text
    if "all" in txt:
        s=0
        c=0
        await message.edit(f"**Unbanning every memeber of chat {message.chat.id}**")
        for member in await app.iter_chat_members(message.chat.id, filter="kicked"):
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

