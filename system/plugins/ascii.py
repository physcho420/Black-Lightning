# Copyright (C) 2021 KeinShin@Github.

import logging
from art import *
import pyrogram

from collections import OrderedDict


from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.types.messages_and_media.message import Message
from system import light
from system import app, HNDLR, COMMAND_HELP
from system.Config.utils import language
from system.Config import Variable
from pyrogram import filters
import importlib


@light.on(["asci"])
async def ascii(client, message):
    txt=message.text.split()[1]
    msg= message.text
    if msg is None:
        a=art("random")
        await message.edit(a)
    try:

     if " " in msg:
         ar = art(txt)
         await message.edit(ar)
    except BaseException as e:
        await message.edit(f"**{e}**")

dictionary = {"alive": "anmol",
               "ascii": "art",
               "sed": "anmol"}

x = dictionary
a = ({k: v for k, v in sorted(x.items(), key=lambda item: item[1])})
COMMAND_HELP.update({'ascii': f"""{HNDLR}ascii or {HNDLR}ascii (text)""",
                      "ascii's help": f"""**USE**:- __{language("Creates random ascii art faces if it's 'NONE' else same face as your given condition")}__ OWO"""})


# for i in a:
#     print(i)

# Python code to demonstrate 
# finding duplicate values from a dictionary
  
# initialising dictionary
# ini_dict = a
  
# printing initial_dictionary
# print("initial_dictionary", str(ini_dict))
  
# finding duplicate values
# from dictionary
# using a naive approach
# rev_dict = {}
  
# for key, value in ini_dict.items():
#     rev_dict.setdefault(value, set()).add(key)
      
# result = [key for key, values in rev_dict.items()
#                               if len(values) > 1]
  
# # printing result
# print("duplicate values", str(result))