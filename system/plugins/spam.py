"""
A Plug to be ported
"""

# import asyncio

# from userbot.utils import admin_cmd, sudo_cmd


# @bot.on(admin_cmd(pattern="spam"))
# @bot.on(sudo_cmd(pattern="spam", allow_sudo=True))
# async def bigspam(blac):
#     if not blac.text[0].isalpha() and blac.text[0] not in ("/", "#", "@", "!"):
#         blac_msg = blac.text
#         blacbot_count = int(blac_msg[9:13])
#         blac_spam = str(blac.text[13:])
#         message = blac.media
#         if message:

#            for i in range(1, blacbot_count):
#              await bot.send_message(message.chat.id ,file=message)
#         else:
#             for i in(1, blacbot_count):
#              await bot.send_message(message.chat.id ,message)

#         await blac.delete()

