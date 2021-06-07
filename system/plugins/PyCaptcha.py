
 # Copyright (C) 2021 KeinShin@Github. All rights reserved





"""
Special Thanks to inuka <3

"""
import time

from PIL import Image
  # Welcome message

from random import randint
import asyncio
from captcha.audio import AudioCaptcha
import importlib
import logging
from pyrogram import filters, emoji
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from system import ASSISTANT_HELP, COMMAND_HELP, app, bot, HNDLR
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPermissions, KeyboardButton, InputMediaPhoto
import random
from math import ceil

from system.datas_sqlite.captcha_sqlite import *

import sys
from system.plugins import light

import os



def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


def create_random_digital_text(string):
    
    captcha_string_list = []
    for i in range(10):
        char = random.choice(string)
        captcha_string_list.append(char)
        
    captcha_string = ''

    # Convert the digital list to string.    
    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string



number_list = ['0','1','2','3','4','5','6','7','8','9']

alphabet_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def create_random_captcha_text(captcha_string_size=10):
    
    captcha_string_list = []

    base_char = alphabet_lowercase + alphabet_uppercase + number_list

    for i in range(captcha_string_size):

        # Select one character randomly.
        char = random.choice(base_char)

        # Append the character to the list.
        captcha_string_list.append(char)

    captcha_string = ''

    # Change the character list to string.    
    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string



def create_random_digital_text(captcha_string_size=10):
    
    captcha_string_list = []
    # Loop in the number list and return a digital captcha string list
    for i in range(10):
        char = random.choice(number_list)
        captcha_string_list.append(char)
        
    captcha_string = ''

    # Convert the digital list to string.    
    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string
def pref(func): 
    # storing the function in a variable 
    return func()
# c=[pref(create_random_captcha_text) for _ in range(100)]
# cp = []
# for i in c:
#      cp.append(i)
# pos = [0, 1, 2, 3, 5, 6]
# cp.insert(random.choice(pos), "sed")
# print(cp)
def gen_captcha(strings: str =None, prefix = create_random_captcha_text, sed = None, emoji = None):
    hmm = [
            (
                InlineKeyboardButton(
                    text="Voice",
                    callback_data="voice_{}".format(strings)
                ),
                
            )
        ]
   
    strings_ = pref(prefix)

    number_of_rows = 10
    number_of_cols = 6
    strings = strings


    c=[pref(prefix) for _ in range(100)]
    cp = [strings,]

    for i in c:
         cp.append(i)
    modules = [  
    
        InlineKeyboardButton(
            text=x,
            callback_data=f"captcha_{x}_{strings}",
        )
        
        for x in cp
    ]

    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    pg_num = 0 % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            pg_num * number_of_rows : number_of_rows * (pg_num + 1)
         ] + hmm
    return pairs

from captcha.image import ImageCaptcha


@bot.on_callback_query(filters.regex(pattern="captcha_(.*)_(.*)"))
async def ho(client, message: CallbackQuery):
    # if not message.from_user.is_restricted:
    #  await message.answer("Um, you can speak freely, so why touching?")
    #  return
    image = message.matches[0].group(1)
    string = message.matches[0].group(2)
#     if message.from_user.id != message.from_user.id:
#         await client.answer_callback_query(message.id,text="Um, Not for you",
#     show_alert=False
# )       
#         return
#     print(message.from_user.id)
    if image == string:
            await message.answer( "✅", show_alert=False)
            render(message.from_user.id)
            print(string)
            await bot.restrict_chat_member(message.message.chat.id,message.from_user.id, ChatPermissions(can_send_messages=True)) 
            ids= message.inline_message_id
            await message.message.delete()
            
  

    elif image != string:
          await message.answer("Try again", show_alert=False)
           
          turns(message.from_user.id)

    elif int(chances(message.from_user.id)[0][1]) == 6:
        await bot.send_message(message.inline_message_id, "User failed to verify them self! try again")

@bot.on_callback_query(filters.regex(pattern="voice_(.*)"))
async def ho(client, message: CallbackQuery):
    string =message.matches[0].group(1)
    sed = create_random_digital_text()
    audio_captcha = AudioCaptcha()
    
    # Because we use the default module voice library, so we can only generate digital text voice.
    string_ = create_random_digital_text()
    # Generate the audio captcha file.
    audio_data = audio_captcha.generate(string_)

    # Save the autiod captcha file.
    audio_file = "./system/temp_files/"+string_+'.wav'
    audio_captcha.write(string_, audio_file)
    image_captcha = ImageCaptcha()
    image = image_captcha.generate_image(string_)

    img  = create_img(image)
    await message.edit_message_media(InputMediaPhoto(img))

    await message.edit_message_reply_markup(InlineKeyboardMarkup(gen_captcha(string_, create_random_digital_text)))
    msg=await bot.send_message(message.message.chat.id, "Creating a Voice Captcha")
    await asyncio.sleep(2)
    msg=await msg.edit("Voice Captcha Generated")
 


    sed=await msg.reply_audio(audio="./system/temp_files/"+string_+'.wav')

    
    await asyncio.sleep(2)
    await msg.delete()
def counter(func):
      def wrapper():
       get_chat()
    # Call the function being decorated and return the result
       return func()
  # Return the new decorated function
      return wrapper







@light.on("captcha",)
async def cap(client, message):
    txt = message.text
    try:
      if " " in txt:
        chet = txt.split()[1]
        try:
  
          add_chat(chet)
        except OperationalError:
            create_table()
            add_chat(chet)
      else:
          chet =message.chat.id
          try:
    
            add_chat(chet, int_=True)
          except OperationalError:
              create_table()
              add_chat(chet, int_=True)
      await message.edit(f"**Captcha Is on for chat** `{chet}`")
    except BaseException as e:
        await message.edit(f"**Can not enable captcha as**\
        \n**ERROR** - `{e}`")

@light.on("reset")
async def sed(client, message):
    txt  = message.text
    if "captcha" in txt:
     await message.edit("**Captcha Reset**")
     reset()



def create_img(img):
        img.save("update.png")
        size = 128, 128       

        basewidth = 300
        img = Image.open('update.png')
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save('ok.jpg')
        return "ok.jpg"


chats=get_chat()
@bot.on_message(filters.chat(chats) & filters.new_chat_members)
async def v(client, message: Message):
    try:
        new_members = [u.mention for u in message.new_chat_members]
        MESSAGE = "{} Welcome to @{}'s group chat {}!"
        text_ = MESSAGE.format(emoji.SPARKLES, message.chat.username,", ".join(new_members))
        await bot.restrict_chat_member(message.chat.id,message.new_chat_members[0].id, ChatPermissions(can_send_messages=False)) 
        msg=await bot.send_message(message.chat.id, "Generating Captcha.")
        await asyncio.sleep(2)
        image_captcha = ImageCaptcha()
        text=create_random_captcha_text()
        image = image_captcha.generate_image(text)

        image.save("captcha.png")
        size = 128, 128       

        basewidth = 300
        img = Image.open('captcha.png')
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save('ok.jpg')
        await msg.delete()
        await  bot.send_photo(message.chat.id, 'ok.jpg', reply_markup=InlineKeyboardMarkup(gen_captcha(text)) ,caption=f"{text_}\n\n**Captcha Feauture by [Black Lightning](htt)**")
        os.remove("captcha.png")
        os.remove("ok.jpg")
    except ChatAdminRequired:
        logging.info(f"ERROR CHAT ADMIN REQUIRED CHAT - @{message.chat.username}")
    # except BaseException as e:
    #     logging.error(f"ERROR WHILE GENERATING CAPTCHA IN CHAT @{message.chat.username} - {sys.exc_info()}")





COMMAND_HELP.update({
    "PyCaptcha": f"{HNDLR}captcha <msg in any chat>",
    "PyCaptcha's help": "**USE**: __Head to assistant help menu as the activation from ur sideand  the module is for assitant__"
})

ASSISTANT_HELP.update({
    "PyCaptcha": "**USE**: __Creates an captcha when user is joined__"
})