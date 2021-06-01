import sqlite3
from system import OWNER




owner = OWNER.replace("@", "").lower()
def Connect():
    conn = sqlite3.connect(f"{owner}.db")
    return conn

    
conn = Connect()
c = conn.cursor()
