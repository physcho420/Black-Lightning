# #   Copyright (C) 2021 KeinShin

# from zeda.sqls import admin_sql
# from zeda.sqls.botusers_sql import *
# from zeda.sqls.admin_sql import *
# from zeda import bot
# import asyncio
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import text

# from zeda.user_bot_assistant import ASSISTANT_HELP, ass_cmd_hndlr

# from telethon import *
# a = []
# import os
# import io

# global tru
# def ADMINS(): 
#     sed=[]

#     for i in str(users()):
#         sed.append(i)

#     return sed

# omk = ADMINS()
# omk=', '.join(omk)
# @tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}promote", from_users=omk ))
# async def admins(event):
#     msg = await event.get_reply_message()
    
#     if event.fwd_from:
#         return
#     async with tgbot.conversation(event.chat.id) as conv:

#      if admin_sql.is_admin(msg.id):
       

#          await conv.send_message('You are already an admin!')
#      else:
      
#          await conv.send_message('Input Userid')
#          id = await conv.get_response()
#          await conv.send_message(f'Sucessfully Promoted user {id}')
#          admin_sql.make_admin(id)
#          add_me_in_db(id)
#     # elif



# #    Copyright (C) Midhun KM 2020

# def starkusers(event):
#     if event.query.user_id == bot.uid:
  
#         total_users = users()
#         users_list = "Tottal Admins\n\n"
#         for starked in total_users:
#             users_list += ("==> {} \n").format(int(starked.chat.id))
#         with io.BytesIO(str.encode(users_list)) as tedt_file:
#             tedt_file.name='adminslist.txt'
#             return tedt_file




# from zeda.user_bot_assistant import oowner
# from zeda.user_bot_assistant._admin_prev import AdminRank, aDmin as admin

# very_Ded2 = oowner()
# very_Ded2 = very_Ded2.wah 

# @tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}demote", from_users=omk))
# async def kooladmins(event):
#     msg = await event.get_reply_message()
    
#     if event.fwd_from:
#         return
#     async with tgbot.conversation(event.chat.id) as conv:

#      if admin_sql.demote(msg.id):
       

#          await conv.send_message('You are already an admin!')
#      else:
      
#          await conv.send_message('Enter Userid who you want to demote')
#          id = await conv.get_response()
#          await conv.send_message(f'Sucessfully Promoted user {id}')
#          admin_sql.demote(id)
#     # elif

# Session = sessionmaker()


# from var import Var
# session = Session()

# tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}admin(r|g)?(.*)", from_users=very_Ded2.id))
# async def admins(event):
#     rank = int(event.pattern_match.group(1))

#     if rank == "r" and " " in rank:

#      rank, name = rank.split(" ")

#      AdminRank = AdminRank(str(name), rank)

#      AdminRank.rnk(event.chat.id, rank)

#      Admin = AdminRank()
     
#      for Rank, in session.query(admin().rank).\
#             filter(admin().name==f'{name}'):
#       await tgbot.send_message(event.chat.id, "The current rank for admin {} is {}".format(name, Rank))
#     if rank == "g":
#      rank, inte = rank.split(' ')
    
#      if inte is None:
#       a = filter(text(rank='{}'.format(inte))).all()
#       await tgbot.send_message(event.chat.id, f"**Total admins with rank {inte} are**\n\n`{a}`")     
#      admin = admin.prom(name=f"{name}", rank=f"{rank}", get=True)
#      for instance in session.query(admin).order_by(admin.id):
#          s =  instance.name, instance.rank
#          await bot.send_message(event.chat.id, s)
#          await asyncio.sleep(0.9)



# @tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}totaladmins", from_users=very_Ded2.id))
# async def admins(event):
#     if admin().id>6:

#      await bot.send_message(event.chat.id, '**Total admins of {} are {}**\n\nWew. too much admin O_O'.format(Var.TG_BOT_USER_NAME_BF_HER, admin().id))

#     elif admin().id is None:
#      await bot.send_message(event.chat.id, '**No current admin of {}** X_X'.format(Var.TG_BOT_USER_NAME_BF_HER))

# ASSISTANT_HELP.update({
#     "admin": "Admin Command",
#     "admin's Type":  "Owner",
#     "Command": f"{ass_cmd_hndlr}promote | {ass_cmd_hndlr}demote\
#     \n**Usage**: Promotes the input user id as your bot admin\
#     \n{ass_cmd_hndlr}prom rank (usernam), (rank)\
#     \n{ass_cmd_hndlr}totaladmins (gets total admin promoted)\
#     \nDisclaimer: He / She can use such commands like {ass_cmd_hndlr}alive, {ass_cmd_hndlr}hack, etc. when you promote them as admin\
#     \n\n"
# })