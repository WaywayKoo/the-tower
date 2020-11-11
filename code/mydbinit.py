import os
try:
    os.unlink('gamett.db')
except:
    print('首次建檔')

import sqlite3
conn = sqlite3.connect('gamett.db')
cur = conn.cursor()

def show_all_rows(all_rows):
    for row in all_rows:
        print(row)
    print()

# 單字表
cur.execute('''CREATE TABLE SETTINGS (ID text, VALUE integer)''')
# 單字表初始資料
cur.execute("INSERT INTO SETTINGS VALUES ('defp', 5)")
cur.execute("INSERT INTO SETTINGS VALUES ('atkp', 20)")
cur.execute("INSERT INTO SETTINGS VALUES ('matkp', 10)")
cur.execute("INSERT INTO SETTINGS VALUES ('player_h', 100)")
cur.execute("INSERT INTO SETTINGS VALUES ('b1_def', 5)")
cur.execute("INSERT INTO SETTINGS VALUES ('b1_atk', 10)")
cur.execute("INSERT INTO SETTINGS VALUES ('b1_h', 100)")


cur.execute('''CREATE TABLE PLAYER (ID text, NAME text, GENDER integer, BIRTH text)''')
cur.execute(" INSERT INTO PLAYER VALUES ('GOD the WK', 'William Ku' , '1', '2005/2/10') ")

cur.execute('''CREATE TABLE SAVE_FILE (ID text, TYPE text, TYPE_NAME text, TYPE_VALUE integer)''')
cur.execute(" INSERT INTO SAVE_FILE VALUES ('GOD the WK', 'item', 'cake', 30)")
cur.execute(" INSERT INTO SAVE_FILE VALUES ('GOD the WK', 'item', 'pie', 20 )")
cur.execute(" INSERT INTO SAVE_FILE VALUES ('GOD the WK', 'item', 'crazy juice', 100 )")
cur.execute(" INSERT INTO SAVE_FILE VALUES ('GOD the WK', 'item', 'banana', 15 )")
cur.execute(" INSERT INTO SAVE_FILE VALUES ('GOD the WK', 'item', 'water', 10 )")
cur.execute(" INSERT INTO SAVE_FILE VALUES ('GOD the WK', 'set', 'layer', 1)")
cur.execute(" INSERT INTO SAVE_FILE VALUES ('GOD the WK', 'set', 'mana', 100)")
conn.commit()

# 查詢player
cur.execute("SELECT * FROM PLAYER")
show_all_rows(cur.fetchall())

cur.execute("SELECT * FROM SAVE_FILE")
show_all_rows(cur.fetchall())
# 查詢設定表
cur.execute("SELECT * FROM SETTINGS")
show_all_rows(cur.fetchall())

# # 成績表
# cur.execute('''CREATE TABLE SCORES
#     (ID integer, ACCOUNT text, TYPE text, SCORE integer, DATE_TIME text)''')

show_all_rows(cur.fetchall())

# 查詢成績表
# cur.execute("SELECT * FROM SCORES")
conn.close()
