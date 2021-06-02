  
# Copyright (C) 2021 KeinShin@Github.





import pickle
import pandas as pd
from typing import Dict
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import random
from pyrogram.errors.exceptions.bad_request_400 import (MessageIdInvalid,
AboutTooLong,
BotInlineDisabled, PasswordEmpty,





)
import os
from pyrogram.sync import wrap
from system.Config import Variable
from system.Config.utils import *
ERRORS_NAME = []

from pyrogram.types import Message
import system
from pyrogram.handlers import MessageHandler

import inspect
from pyrogram import filters, ContinuePropagation

from system.Config import *
from system.Config.errors import *
import logging

time = datetime.datetime.now()

SUDO_USER_NO_OF_TIME_USED = {}
s = []
easters = []
ASSIS_HELP = {}
 # it is test sur






# pyrogram.types.User.last_online_date()



class light:



     def on(self, cmd, sudo_ids  = None,  grup: int = -1):
            self.command = cmd
            self.id = sudo_ids
            self.hndlr = system.HNDLR
            self.grup = grup
            if Variable.HNDLR is None:
                  raise HNDLRERROR(f"{language('You are  not allowed to leave HNDLR None.')}")

    


            if not self.id:
              self.filter = ((filters.me | filters.user(self.id)) & filters.command(self.command, self.hndlr) & ~filters.via_bot & ~filters.forwarded)
            else:
              self.filter =       (filters.me & filters.command(self.command, self.hndlr) & ~filters.via_bot & ~filters.forwarded)
    
            try: 
             c = " ".join(self.command)
             system.CMD_LIST.append(c[0:])
            except BaseException as e:
             logging.info(e)
            def handle(function):

                   async def call(client, message):
                  # off course basic help fron friday  for decorator.
                       try:
                         await function(client, message)
                       except ContinuePropagation:
                         raise ContinuePropagation
                   system.app.add_handler(MessageHandler(call, filters=self.filter), group=self.grup) # sorry TwT

                   return call
            return handle


class schedule(light):

     def schedule(self,
     stime:int = 0,
     time = None,
     name = None
     ):

             if time == "seconds":
       
                 scheduler = AsyncIOScheduler()
     
     
                 
                 scheduler.add_job(job, 'interval', seconds=int(stime), id=name)
             if time == "minute":    
                 scheduler.add_job(job, 'interval', minute=int(stime), id=name)




     async def scheduler(message,
     shutdown:bool =False,
     resume:bool = False):
         scheduler = AsyncIOScheduler()
         scheduler.pause()
         await message.edit(f"**All! {language('scheduling task that are paused')}**.")
         if shutdown is True:
          try:   
             scheduler.shutdown()
             await message.edit(f"**{language('scheduler is shutdowned')}**")
          except Exception as e:
              await message.edit(e)
         elif resume is True:
             try:
                 scheduler.resume()
                 await  message.edit(f"**{language('All tasks are resumed')}**")
             except Exception as e:
                await message.edit(e)



def owner(func):
 pass

# function




def inline_help_wrapprs(func):
    async def wrapper(client, really):
        bot = await system.bot.get_me()
        i = bot.id
        if really.from_user.id == i:
           really.answer(f"{language('Get Lost Retard')}", cache_time=0, show_alert=True)
        else:
            
            try:
                await func(client ,really)
            except Exception as e:
                logging.error(e)  

    return wrapper 






