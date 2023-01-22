import sys
sys.path.append('../')
import system.global_value as g

import requests
import json
import MySQLdb

def receive(gameid):
    # データベースへの接続
    con = MySQLdb.connect(
        host='',
        user='',
        passwd='',
        db=''
    )
    cur = con.cursor()

    # slackメッセージ受信設定
    cur.execute("SELECT * FROM main WHERE id = "+ gameid)