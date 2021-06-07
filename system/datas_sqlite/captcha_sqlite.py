from system.datas_sqlite.afk_sqlite import ex
from system.datas_sqlite import c, conn

from collections import *

from sqlite3 import *
def create_table():
    try:

      c.execute(f"""CREATE TABLE captcha (
            chat TEXT,
            id INTEGER
            )""")
      conn.commit()
    except OperationalError:
        pass
  

    try:
      c.execute(f"""CREATE TABLE ded (
          user_ TEXT,
          sed TEXT
          )""")
      conn.commit()

    except OperationalError:
        pass

    try:
      c.execute(f"""CREATE TABLE chances (
          user TEXT,
          chance TEXT
          )""")
      conn.commit()
    except OperationalError:
        pass

def add_chat(chat, int_: bool =False):
    if int_:

       c.execute("INSERT INTO captcha VALUES (?, ?)", (0, chat,))
   
   
       conn.commit()
    else:

       c.execute("INSERT INTO captcha VALUES (?, ?)", (chat, -100))
   
       conn.commit()
def get_chat():
    chats = []
    c.execute("SELECT * FROM captcha")

    a = c.fetchall()
    for i in a:
       a=i[0]
       b=int(i[1])
       chats.append(a)
       chats.append(b)
    chats= list(OrderedDict.fromkeys(chats))
    return list(chats)
print(get_chat())

def chances(user, captcha: bool= False):
    if captcha:
      c.execute(f"SELECT * from ded WHERE user_ == {user}")
      s = c.fetchone()
      return [s]
    else:
      c.execute(f"SELECT * from chances WHERE user == {user}")
      s = c.fetchone()
      return [s]



def turns(user):
    c.execute("INSERT INTO chances VALUES (?, ?)", (user, 0))
    conn.commit()
    c.execute(f"UPDATE chances SET chance = chance  + 1 WHERE user == {user}")
    conn.commit()

def render(user):
    c.execute("INSERT INTO ded VALUES (?, ?)", (user, 0))
    conn.commit()

    c.execute(f"UPDATE ded SET sed = sed  + 1 WHERE user_ == {user}")
    conn.commit()

def reset():
    try:

     c.execute("DROP TABLE captcha")
     conn.commit()
    except OperationalError:
  
        pass


