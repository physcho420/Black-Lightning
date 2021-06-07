# Copyright (C) 2021 KeinShin@Github.
import asyncio
from inspect import Attribute
import subprocess

import os.path
import sys

from setup.importer import Start
import pickle as yum
import logging 
import sys, traceback
import heroku3



import schedule
from pyrogram.handlers import MessageHandler
import system
from pyrogram import idle, filters
from pyrogram.types import Message
from pyrogram.errors import *
from system.Config.utils import Variable
from pyrogram.raw.types import BotCommand
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
import holidays
from datetime import date, datetime


Heroku = heroku3.from_key(Variable.HEROKU_API_KEY)
if Variable.COUNTRY:
    
   hol  = holidays.CountryHoliday(Variable.COUNTRY)
else:
   hol = holidays.CountryHoliday("IN", prov="AS")
a = date.today()
p  =hol.get(a)



plugin =  logging.getLogger("PLUG-ERROR")
bot_lod =  logging.getLogger("BOT-ERROR")


from system.__init__ import app, bot





app = app


async def start_up(client, message:Message):
    from system import app, bot
    await message.edit("**Auto Mating Tasks**")
    s = await bot.get_me()
    me = await app.get_me()
    happ = Heroku.app(Variable.HEROKU_APP_NAME)
    var = happ.get_config()
    await asyncio.sleep(1)
    # if message.chat.id != (await app.get_me()).id:
        # await message.edit("Startup Command that can be executed in ")
 
    await message.edit("**Creating Logs Channel**")

    await asyncio.sleep(1)

    if Variable.LOGS_CHAT_ID is None:
      ch=  await app.create_group("Lightning's Userbot Traceback/Logs", me.id )
      ch=ch.id
       
      var["LOGS_CHAT_ID"] = ch
      try:

       await bot.join_chat(ch)
       text = f"Assistant  has been successfully connected to logs channel and deployed."
       await bot.send_message(chet, text)
    
      except UserAlreadyParticipant:
        pass
    await message.edit("**Putting your username**")
    
    await asyncio.sleep(1)
    if Variable.OWNER_NAME is None:
        var["USER_NAME"] =  f"@{me.username}"

    await message.edit("**Putting bot's username**")

    await asyncio.sleep(1)
    if Variable.TG_BOT_USER_NAME is None:
        var['TG_BOT_USER_NAME'] = f'{s.username}'
    
chet = Variable.LOGS_CHAT_ID


USER = str(Variable.OWNER_NAME)

async def easter():
    # if Variable./
    est=yum.load("easters.dat", "rb") # for easters!
    if len(est)==7:
        await bot.send_message(chet, "**Congo**, **You have unlocked all the easters of this userbot gib party sir** 🎉🎆")

async def holydays():
    if p:
        await bot.send_message(chet, f"Happy {p} Master ✨🎉☺")
    else:
        return None


schedule.every().day.at("12:00").do(holydays)



async def add_bot_to_logg_grup(client, message):
    try: 

        await bot.join_chat(chet)
        text = f"BLACK USERBOT is deployed."

        await bot.send_message(chet, text)
    except BaseException:

        logging.error("CANNOT ADD ASSISTANT TO LOGS CHAT")
        pass
        


# import glob
# import importlib



import logging
import os
import importlib
import pyrogram
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)


from  system import bot, app

def o():
    try:
        a = Start("system/plugins/")
        for  i in a.x:
                # try:

                 a.pat = i.replace(".py", "")   
                 a.boot()
    
                 logging.info("IMPORTED PLUGINS- {}".format(i))
                # except Exception:
                #   logging.error(f"ERROR NOT LOADED - {i} - {sys.exc_info()}")
        a = Start("system/user_bot_assistant/")
        for  i in a.x:
            try:
             a.pat = i.replace(".py", "")   
             a.boot()
             logging.info("IMPORTED ASISSTANT MODULE- {}".format(i))
            except Exception:
             logging.info(f"ERROR NOT LOADED {i} - {sys.exc_info()}")
    except ImportError:
    
     s=sys.exc_info()
     logging.error(f"ERROR - {s}")
     pass
    except ModuleNotFoundError:
     s=sys.exc_info()
     logging.error(f"ERROR - {s}")
     pass
    except BaseException:
        yo=traceback.TracebackException(*sys.exc_info())
        try:
           name=yo.filename
           no = yo.lineno
           line = yo.lineno
           type_=yo.exc_type
        except AttributeError:
            pass
        logging.info(f"There is an error - {type_} in file {name} line {no} - {line}, In order to prevent crash it has been renamed and plugins based on this file wont work!")
        logging.info("Contact @lightning_support_group When to update!")
        filename_ = name.replace(".py", ".txt")
        os.rename(name, filename_)
        os.remove(name)
        importlib.import_module("system.plugins.Pgit")
        logging.info("Only Updater will work from now util u update a fix the bug :P! with")
        app.run()
        return
if __name__ == "__main__":
    logging.info("Setting up")
    o()
    app.add_handler(MessageHandler(start_up, filters.command("setup", ".") & filters.me))
    try:
        try:   
       
          bot.start()
    
          try:
      
            bot.join_chat(chet)
            
            text = f"BLACK USERBOT has been deployed."
            bot.send_message(chet, text)
          except UserAlreadyParticipant:
            pass
    
        except BaseException:
           logging.error("CANNOT ADD ASSISTANT TO LOGS CHAT")
           pass
        except SessionExpired:
            logging.info("Your String Session is not valid create a new one for more contact @lightning_support_group, till bot stopped")
            exit(1)
            
        except SessionRevoked:
             logging.info("Bot Father Api Token Revoked replace old with new one till bot stopped")
             exit(1)
        except AuthKeyDuplicated:
             logging.error("You can not use same token in two or more apps/client, stop one token!")
             exit(1)
        except AccessTokenInvalid:
            logging.error("Bot token expired or not valid create new one.")
            exit(1)
        except AccessTokenInvalid:
            logging.error("Bot token not valid")
            exit(1)
        try:
         logging.info(f"© Black-Lightning - KeinShin, All  rights Reserved.")
         logging.info(f"Plugins and Whole System Loaded!, do {system.HNDLR}alive to check!")
         logging.info(f"Also add assistant to log channel to access more features!")
         app.start() 
         idle()
        except SessionRevoked:
           logging.error("String Session Revoked or Terminated! Create a new one")
           exit(1)
        except SessionExpired:
            logging.info("Your String Session is not valid create a new one for more contact @lightning_support_group, till bot stopped")
            exit(1)
        except AuthKeyDuplicated:
             logging.error("You can not use same strings in two or more apps/client, terminate one of create another")
             exit(1)
    except ApiIdInvalid:
        logging.error("The Given Api Id is invalid,  grab ur Id from my.telegram.org Now!")
        exit(1)



