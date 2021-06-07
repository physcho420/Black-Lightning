# Copyright (C) 2021 KeinShin@Github.


from telegraph import Telegraph
from telegraph import upload_file
from system import light
from system import *
telegraph = Telegraph()

telegraph.create_account(short_name='TG_UB')


@light.on(["telegraph"])
async def tg(client, message):
    # if not message.photo or message.sticker or message.video  :
    #     await message.edit("**Are you sure this is media?**")
    #     return
    a = message.reply_to_message.photo.file_id
    a=await app.download_media(a)
    a=upload_file(a)
    o = 'http://telegra.ph/{}'.format(a)
    await app.send_message(message.chat.id, f"__YOUR LINK SIR__\n\n{o}")


COMMAND_HELP.update(
    {"telegram_link": f"{HNDLR}telegrah",
    "telegram_link_": f"Tool",
    "telegraph_link's help": f"Creates telegraph link for the given media can image or video"}
)