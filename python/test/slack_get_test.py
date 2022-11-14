import requests
from datetime import datetime
import json
import time

# slack appのwerewolfのUser OAuth Tokenを指定
TOKEN = 'xoxp-3157585096822-3161337001733-4377923093681-7006a0f57b7c33ee234480f0145931be'    
CHANNEL = 'C0356QW1GKB'    # チャンネル:postを指定
user_id = 'U034R9X01MK'    # userのid、現在はkyle440440を指定

url = "https://slack.com/api/conversations.history"
headers = {"Authorization": "Bearer "+TOKEN}
params = {
   "channel": CHANNEL,
   "limit": 1
}

def wait_player_message():
   while True:
      r = requests.get(url, headers=headers, params=params)
      json_data = r.json()
      msgs = json_data['messages'][0]

      if ('user' in msgs):    # in演算子でjson内にusernameというkeyがあるならTrue、ないならFalse
         user_name = msgs['user']
         if (user_name == user_id):
               text_content = msgs['text']
               print("入力完了")
               return text_content
      
      print("入力待ち")
      time.sleep(5)

player_action = wait_player_message()
print(player_action)