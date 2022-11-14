# 乱数発生
import random
# slack接続用
import requests     # pip install requests
import json
# 時間計測
import time
# これ何に使ってるか不明
from datetime import datetime

# slackメッセージ送信先の定義
## 人狼プログラム設計
#WEB_HOOK_URL = "https://hooks.slack.com/services/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"
#channel_name = "#人狼テスト"

## kyle
# 一個目のはslack appのwebhookのurlなんだけど、ユーザネームとかうまく変えられないからカスタムインテグレーションから使えるwebhookにしてる。
#WEB_HOOK_URL = "https://hooks.slack.com/services/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"
WEB_HOOK_URL = "https://hooks.slack.com/services/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"
channel_name = "#post"

# slackメッセージ受信先の定義
# slack appのwerewolfのUser OAuth Tokenを指定
TOKEN = 'xoxp-3157585096822-3161337001733-4377923093681-7006a0f57b7c33ee234480f0145931be'    
CHANNEL = 'C0356QW1GKB'    # チャンネル:postを指定
user_id = 'U034R9X01MK'    # userのid、現在はkyle440440を指定

# slcakメッセージ受信設定
url = "https://slack.com/api/conversations.history"
headers = {"Authorization": "Bearer "+TOKEN}
params = {
   "channel": CHANNEL,
   "limit": 1
}

# ゲームマスター用メッセージ送信
def system_message(message):
    requests.post(WEB_HOOK_URL, data=json.dumps({
        "channel" : channel_name,
        "text" : message,
        "icon_emoji" : ":gear:",
        "username" : "system"
    }))

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

# テスト用変数
RED = '\033[31m'
END = '\033[0m'
death = 0

# 役の割り振り
player = 10
job = ('人狼', '村人', '占い師')

# プレイヤー名:j=0、好きプレイヤー:j=1、嫌いプレイヤー:j=2、性格:j=3、役職:j=4、生死:j=5(0:生存,1:死亡)
characters = [[chr(ord('A')+i) if j == 0 else chr(ord('A')+random.randint(1, player)) if j == 1 or j == 2 else random.randint(1, 2) if j == 3 else random.choice(job) if j == 4 else 0 for j in range(6)] for i in range(player)]
# 好き嫌いのプレイヤーの被り（自分自身、好き嫌いが両方等しい）には対応してない。
# 関数作ってiの値を参照して自分自身が好き嫌いに入らないように調整する。
# 役職はあらかじめ外部で作っておいてそれをcharacters配列に格納する感じで作る。

# 誰が占われたかの配列と投票時の配列が必要

# 確認用
print(characters)

# ゲーム日数の定義
day = 0

# トーク順番の定義
talk_num = 0

# 生存プレイヤー数と死亡プレイヤー数の定義
live_player = player
death_player = 0

# 各陣営の人数の定義
villagers = 0
werewolves = 0
for i in range(player):
    if characters[i][4] == '占い師' or characters[i][4] == '村人':
        villagers+=1
    else :
        werewolves+=1
print('村人陣営：', villagers, '人')
print('人狼陣営：', werewolves, '人')

# 村人エージェント
def villager_agent(player_info, operation):
    if operation == 'night':
        pass
    elif operation == 'daytime':
        speak = '村人です'
        return speak
    else:
        pass

# 占い師エージェント
def diviner_agent(player_info, operation):
    if operation == 'night':
        pass
    elif operation == 'daytime':
        speak = '占い師です'
        return speak
    else:
        pass

# 人狼エージェント
def werewolf_agent(player_info, operation):
    if operation == 'night':
        pass
    elif operation == 'daytime':
        speak = '人狼です'
        return speak
    else:
        pass

info = '人狼ゲームを開始します。'
system_message(info)

# ゲーム進行のループ
while True:
    # 日付の変更
    info = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print(info)
    day+=1

    # 夜の処理
    state = 'night'
    requests.post(WEB_HOOK_URL, data=json.dumps({
    "channel" : channel_name,
    "text" : "夜になりました。",
    "icon_emoji" : ":full_moon:",
    "username" : "time"
    }))
    info=str(day)+'日目の夜です。'
    print(info)
    system_message(info) 

    # プレイヤーの行動
    if characters[0][5] == 0:
        # 役職の説明
        info = 'あなたの役職は'+characters[0][4]+'です。\n'
        #info = RED+info+END
        print(info)
        #system_message(info) # 役職の開示は各役職の行動にくっつける

        # 各役職の行動
        if characters[0][4] == '村人':
            info = info + '怪しいと思う人を選んでください。'
            #info = RED+info+END
            print(info)
            system_message(info) 
            #input()
            player_action = wait_player_message()      
            #最終的には次の日に怪しい人をエージェントからも募って発表する
        elif characters[0][4] == '占い師':
            info = info + '占いたい人を選んでください。'
            #info = RED+info+END
            print(info)
            system_message(info) 

            # テスト用 占い者決定
            #divination = random.randint(0,player-1)
            #info = characters[divination][0]+'は'+characters[divination][4]+'です。'
            #info = RED+info+END

            #input()
            count = player
            while True:
                if count == player:
                    player_action = wait_player_message()
                count %= player
                if characters[count][0] == player_action and characters[count][5] == 0:
                    info = characters[count][0]+'は'+characters[count][4]+'です。'
                    break     
                count += 1 
                if count == player:
                    info = '指定が誤っています\nもう一度、占いたい人を選んでください。'   
                    print(info)
                    system_message(info)        
        
            print(info)
            system_message(info) 

        else:
            # だれが味方か表示する
            info = info + '殺したい人を選んでください。'
            #info = RED+info+END
            print(info)
            system_message(info) 
            
            # テスト用 犠牲者決定
            #while True:
            #    bite = random.randint(0,player-1)
            #    death = 1
            #    if characters[bite][4] != '人狼' and characters[bite][5] == 0:
            #        break

            #input()
            count = player
            while True:
                if count == player:
                    player_action = wait_player_message()
                    print(player_action)
                count %= player
                print(characters[count][0])
                if characters[count][0] == player_action and characters[count][5] == 0 and characters[count][4] != '人狼':
                    victim = characters[count][0]
                    characters[count][5] = 1
                    info = characters[count][0]+'を殺しました。'
                    print(info)
                    death = 1
                    bite = count
                    break     
                count += 1 
                if count == player:
                    info = '指定が誤っています\nもう一度、殺したい人を選んでください。'   
                    print(info)
                    system_message(info)     
            
            print(info)
            system_message(info)

    else: 
        info = 'あなたは幽霊です。'
        #info = RED+info+END
        print(info) 
        system_message(info)       

    # 各エージェントの呼び出し
    for i in range(1, player):
        if characters[i][4] == '村人':
            action = villager_agent(characters[i], state)
        elif characters[i][4] == '占い師':
            action = diviner_agent(characters[i], state)
        else:
            action = werewolf_agent(characters[i], state)

    info = '---------------------------------------------'
    print(info)

    # 昼の処理
    state = 'daytime'
    requests.post(WEB_HOOK_URL, data=json.dumps({
    "channel" : channel_name,
    "text" : "昼になりました。",
    "icon_emoji" : ":sunny:",
    "username" : "time"
    }))
    info=str(day)+'日目の昼です。'
    print(info)
    system_message(info)
    # テスト用 犠牲者決定
    if death == 1:
        death = 0
        info = characters[bite][0]+'が死体となって発見されました。'
        print(info)
        system_message(info)
    else :
        while True:
            bite = random.randint(0,player-1)
            if characters[bite][4] != '人狼' and characters[bite][5] == 0:
                break
        victim = characters[bite][0]
        characters[bite][5] = 1
        info = characters[bite][0]+'が死体となって発見されました。'
        print(info)
        system_message(info)
    
    # 夜明けのゲーム終了条件の確認
    villagers-=1
    live_player-=1
    death_player+=1
    if villagers <= werewolves:
        info = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print(info)
        info = '人狼陣営が勝利しました'
        print(info)
        system_message(info)
        break

    # 会話の処理
    #talk_num = 0
    info = '人狼を見つけるために話し合ってください。'
    print(info)
    system_message(info)
    start = time.time()
    while True:
        talk_num %= player
        if talk_num == 0:
            #info = '発言内容を選んでください。'
            #print(info)
            #action = input()
            player_action = wait_player_message()
            if player_action == "break":
                break
        elif characters[talk_num][4] == '村人' and characters[talk_num][5] == 0:
            action = villager_agent(characters[talk_num], state)
        elif characters[talk_num][4] == '占い師' and characters[talk_num][5] == 0:
            action = diviner_agent(characters[talk_num], state)
        elif characters[talk_num][4] == '人狼' and characters[talk_num][5] == 0:
            action = werewolf_agent(characters[talk_num], state)

        if talk_num != 0 and characters[talk_num][5] == 0:
            info = characters[talk_num][0] + '：' + action
            print(info)
            # slackに送信
            requests.post(WEB_HOOK_URL, data=json.dumps({
            "text" : action,
            "icon_emoji" : ":hugging_face:",
            "username" : characters[talk_num][0]
            }))
        
        end = time.time()
        talk_num+=1
        if end-start > 30:
            break
        time.sleep(2)

    info = '---------------------------------------------'
    print(info)

    # 投票の処理
    state = 'vote'
    requests.post(WEB_HOOK_URL, data=json.dumps({
    "channel" : channel_name,
    "text" : "夕方になりました。",
    "icon_emoji" : ":Star:",
    "username" : "time"
    }))
    info = 'これより投票を行います。\n人狼だと思う人に票を入れて下さい。'
    print(info)
    system_message(info)
    #player_action = wait_player_message()  
    count = player
    while True:
        if count == player:
            player_action = wait_player_message()
            print(player_action)
        count %= player
        print(characters[count][0])
        if characters[count][0] == player_action and characters[count][5] == 0:
            # 投票の処理
            break     
        count += 1 
        if count == player:
            info = '指定が誤っています\nもう一度、投票先を選んでください。'   
            print(info)
            system_message(info)   

    # 投票（現在は乱数）
    vote_result = random.randint(0,2) # 0:村人陣営死亡, 1:人狼陣営死亡, 2:死亡者なし
    
    # 投票後のゲーム終了条件の確認
    if vote_result == 0:
        #テスト用投票者の決定
        while True:
            voted = random.randint(0,player-1)
            if characters[voted][4] != '人狼' and characters[voted][5] == 0:
                break
        characters[voted][5] = 1
        info = '投票の結果、'+characters[voted][0]+'が処刑されます。'
        print(info)
        system_message(info)

        # 現在の人数の再定義
        villagers-=1
        live_player-=1
        death_player+=1
        if villagers <= werewolves:
            info = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            print(info)
            info = '人狼陣営が勝利しました'
            print(info)
            system_message(info)
            break
    elif vote_result == 1:
        #テスト用投票者の決定
        while True:
            voted = random.randint(0,player-1)
            if characters[voted][4] == '人狼' and characters[voted][5] == 0:
                break
        characters[voted][5] = 1
        info = '投票の結果、'+characters[voted][0]+'が処刑されます。'
        print(info)
        system_message(info)

        # 現在の人数の再定義    
        werewolves-=1
        live_player-=1
        death_player+=1
        if werewolves == 0:
            info = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            print(info)
            info = '村人陣営が勝利しました。'
            print(info)
            system_message(info)
            break
    else:    # 投票によって死人が発生しなかった場合
        info = '本日処刑される人はいません。'
        print(info)
        system_message(info)

