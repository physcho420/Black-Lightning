import sqlite3
import system


from system.Config.utils import Variable
owner =Variable.OWNER_NAME.replace("@", "").lower()
def Connect():
    conn = sqlite3.connect(f"{owner}.db")
    return conn

    
conn = Connect()
c = conn.cursor()
