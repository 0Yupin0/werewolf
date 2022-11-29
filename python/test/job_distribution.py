import random

# 役の割り振り
player = 10                                             # プレイヤー人数の定義
job = ('人狼', '村人', '占い師')                         # 役職の種類の定義
job_balance = [player*0.2, player*0.8, player*0.2]      # 役職の割合の定義

# 各役職の人数の初期化
werewolf_player = 0
villager_player = 0
diviner_player = 0

# 役職の割り振りの関数
# 役職が決めた割合（job_balance）になるように調整
def job_distribution(a):
    global werewolf_player, villager_player, diviner_player
    r = random.choice(job)
    if r == '人狼':
        werewolf_player += 1
        if werewolf_player > job_balance[0]:
            werewolf_player -= 1
            r = job_distribution(a)
    elif r == '村人':
        villager_player += 1
        if villager_player > job_balance[1]:
            villager_player -= 1
            r = job_distribution(a)
    elif r == '占い師':
        diviner_player += 1
        if diviner_player > job_balance[2]:
            diviner_player -= 1
            r = job_distribution(a)
    return r

# プレイヤーの好みのプレイヤーを決定する関数
# 自分自身は好みに入らない。また、一人のプレイヤーの好き嫌いが同じにならないようにする
# 好き嫌いにされるのはそれぞれ一人ずつのみ（多くの人に好かれる、嫌われるということがない）
#player_name = [[chr(ord('A')+i) for i in range(player)] for i in range(2)]
#print(player_name)
#def player_preference(a, b):        # a=, b=j
#    r = chr(ord('A')+random.randint(1, player))
#    if b == 1:
#        for i in range(a):
#            if characters[i][b] == r:
#                player_preference(a, b)
#    elif b == 2:
#        for i in range(a):
#ここから途中

# プレイヤー情報を定義した配列
# プレイヤー名:j=0、好きプレイヤー:j=1、嫌いプレイヤー:j=2、性格:j=3、役職:j=4、生死:j=5(0:生存,1:死亡)
characters = [[chr(ord('A')+i) if j == 0 else chr(ord('A')+random.randint(1, player)) if j == 1 or j == 2 else random.randint(1, 2) if j == 3 else job_distribution(i) if j == 4 else 0 for j in range(6)] for i in range(player)]
# 好き嫌いのプレイヤーの被り（自分自身、好き嫌いが両方等しい）には対応してない。
# 関数作ってiの値を参照して自分自身が好き嫌いに入らないように調整する。
# 役職はあらかじめ外部で作っておいてそれをcharacters配列に格納する感じで作る。

# 各プレイヤーの情報の表示
for i in range(player):
    print(characters[i])

# 誰が占われたかの配列と投票時の配列が必要