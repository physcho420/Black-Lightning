# Copyright (C) 2021 KeinShin@Github. All rights reserved


from collections import OrderedDict
from system.datas_sqlite import c, conn
from sqlite3 import OperationalError
try:
  conn.execute(f"""CREATE TABLE approved_users (
      users TEXT

      )""")
except OperationalError:
    pass
try:
  conn.execute(f"""CREATE TABLE turns (
      id TEXT,
      turn TEXT
      )""")
except OperationalError:
    pass


from system import PM_LIMIT
  
# c.execute("DROP TABLE approved_users")
# conn.commit()



def approve(ids):
    c.execute("INSERT INTO approved_users VALUES (?)", ((ids,)))
    conn.commit()


def approved():

    c.execute("SELECT * FROM approved_users " )
    s = c.fetchall()
    
    return s
sed = False
def all_user():

   approved_ = []
   for i in  approved():
       approved_.append(i[0])
   approved_niggas = list(OrderedDict.fromkeys(approved_))
   return approved_niggas



def disapprove(ida):
    c.execute(f"DELETE from approved_users WHERE users == {ida}")
    conn.commit()

def his_turn(user):

    c.execute(f"SELECT * from turns WHERE id == {user}")
    s = c.fetchone()
    return [s]




def update_turns(user):
    c.execute("INSERT INTO turns VALUES (?, ?)", (user, 0))
    conn.commit()
    c.execute(f"UPDATE turns SET turn = turn + 1 WHERE id == {user}")
    conn.commit()


def turn(ids_, delete = None):
    if delete:
        c.execute("SELECT id DELETE FROM turns WHERE id == ")

    c.execute(f"""SELECT * FROM turns WHERE id == {ids_}""")
    a=c.fetchall()
    ids= {}
    turns = []
    for i in a:
        turns.append(i[0])
        ids.update({
            i[1]: turns
      })
    
    return ids
    
sed=[str(i) for i in range (0, 5)]
sed=" AND ".join(sed)
def remove_user(user_):
    c.execute(f"DELETE  FROM turns WHERE turn = (?, ?, ?, ?){PM_LIMIT} AND id  == {user_}", (sed))
    conn.commit()
print(his_turn(1627708231)[0][1])