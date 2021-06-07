# Copyright (C) 2021 KeinShin@Github.



#  Hello sur 
from typing import *
import requests
import time as t
def clock():
    while True:
        print(datetime.datetime.now().strftime("%I:%M:%S"), end="\r")
        time.sleep(1)
import platform
from system.plugins import light
from system.Config import Variable
from system.Config.utils import  get_readable_time
ping = get_readable_time((t.time() - t.time()))
from system import (ALIVE_IMG, COMMAND_HELP, app, ALIVE_MESSAGE, OWNER, time, ttl, updates, self_hosted, MODE
)        # Easter OwO
if ALIVE_IMG is None:
    ALIVE_IMG = "https://telegra.ph/file/4e83650cf1e3e8c31c51b.mp4"


from datetime import datetime




now = datetime.now()

import datetime
import time

@light.on(["alive"])
async def alivae(client, message):


    if ALIVE_MESSAGE is  None:
      text = f"""
ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ is ᴀᴡᴀᴋᴇɴᴇᴅ
**Owner**-: **__{OWNER}__**
**Time**:  **__{time}__**
**Commands**:  **__{ttl}__**
**Ping**:  **__{ping}__**
**Updates**:  **__{updates}__**
**Self Hosted**:  **__{self_hosted}__**
**Mode**: __**{MODE}**__
**Device Using**: __**{platform.system()}**__
      """
    else:
          
      text = ALIVE_MESSAGE
    if ALIVE_IMG.endswith(".mp4"):


        msg=await app.send_video(message.chat.id, ALIVE_IMG, caption=text)
        if ALIVE_MESSAGE is None:
            while True:
             sed = datetime.datetime.now().strftime("%I:%M:%S")
             time.sleep(6)
             await msg.edit_caption(f"""ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ is ᴀᴡᴀᴋᴇɴᴇᴅ
**Owner**-: **__{OWNER}__**
**Time**:  **__{sed}__**
**Commands**:  **__{ttl}__**
**Ping**:  **__{ping}__**
**Updates**:  **__{updates}__**
**Self Hosted**:  **__{self_hosted}__**
**Mode**: __**{MODE}**__
**Device Using**: __**{platform.system()}**__
      """)
    elif ALIVE_IMG.endswith(".jpg") or ALIVE_IMG.endswith(".png"):
        await app.send_photo(message.chat.id, ALIVE_IMG, caption=text)
    await message.delete()