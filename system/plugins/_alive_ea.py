# Copyright (C) 2021 KeinShin@Github.



#  Hello sur 


from system.decorators import zeda_cmd
from Config import *
from Config.utils import *
ping = get_readable_time((time.time() - last_up))
from system import *              # Easter OwO
@zeda_cmd(["alive", "black", "alv", f"{OWNER}"], sudo=True, sudo_id=Variable.SUDO_IDS)
async def alive(client, message):
 if ALIVE_MESSAGE is not None:

   text = f"""ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ is ᴀᴡᴀᴋᴇɴᴇᴅ
   🇴‌🇼‌🇳‌🇪‌🇷‌-: {OWNER}
   ᴛɪᴍᴇ: {time}
   ᴄᴏᴍᴍᴀɴᴅs: {ttl}
   ᴘɪɴɢ: {ping}
   ᴜᴘᴅᴀᴛᴇꜱ: {updates}
   ꜱᴇʟꜰ ʜᴏꜱᴛᴇᴅ: {self_hosted}
   ᴍᴏᴅᴇ: {mode_type}
   """
 else:
   text = ALIVE_MESSAGE
 await app.send_document(message.chat_id, ALIVE_IMG, caption=text)
 
