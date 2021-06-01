# Copyright (C) 2021 KeinShin@Github.



#  Hello sur 
import time as t


from system.plugins import light
from system.Config import Variable
from system.Config.utils import  get_readable_time
ping = get_readable_time((t.time() - t.time()))
from system import (ALIVE_IMG, COMMAND_HELP, app, ALIVE_MESSAGE, OWNER, time, ttl, updates, self_hosted, MODE
)        # Easter OwO
if ALIVE_IMG is None:
    ALIVE_IMG = "https://telegra.ph/file/4e83650cf1e3e8c31c51b.mp4"



@light.on(["alive"], -1)
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
      """
    else:
      text = ALIVE_MESSAGE
    print("ALIVE")
    if ALIVE_IMG.endswith(".mp4"):
          
        await app.send_video(message.chat.id, ALIVE_IMG, caption=text)
    elif ALIVE_IMG.endswith(".jpg") or ALIVE_IMG.endswith(".png"):
        await app.send_photo(message.chat.id, ALIVE_IMG, caption=text)
          


 
