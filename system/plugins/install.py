import logging
from system import CMD_LIST, app, HNDLR, COMMAND_HELP
from PIL import Image, ImageDraw, ImageFont
from system.plugins import light
import requests
import datetime
import importlib
import imgkit
@light.on(["install"])
async def pl(client, message):
   url = "https://del.dog/documents"
   r = requests.post(url, data=message).json()
   url = f"https://del.dog/{r['key']}"
   end = datetime.now()
   imgkit.from_url(url, "checked.png")
   await app.send_document(message.chat.id, "checked.png", caption=f"**First check secure codes ( for security ) master then reply with `{HNDLR}install now` to install**")

   if "now" in message.text:
    try:
       importlib.import_module("system.plugins.", message.media)
       logging.info("IMPORTED  - {}")
       CMD_LIST.append(message)
    except BaseException as e:
        await message.edit("**")

COMMAND_HELP.update({
    "install": f"`{HNDLR}install` (reply to message)",
    "install_": "help",
    "install's help": "**USE**: Install file in userbott"
})