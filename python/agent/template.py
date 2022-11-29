import random

# プレイ人数の定義
player = 10

# 役職の定義
job = ('人狼', '村人', '占い師')

# 役職の人数割合定義
job_balance = [player*0.2, player*0.8, player*0.2] 

# 各役職の人数の初期化
werewolf_player = 0
villager_player = 0
diviner_player = 0

# 役職の割り振り
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

# プレイヤー情報の定義
characters = [
    [chr(ord('A')+i) 
    if j == 0 else random.randint(1, 2) 
    if j == 1 else job_distribution(i) 
    if j == 2 else 0 
    for j in range(4)] 
    for i in range(player)]

# プレイヤー情報の表示
for i in range(player):
    print(chr(ord('A')+i),"：",characters[i])

# 推理データの作成
inference = [[
    [50 if j != 3 else random.randint(30,71) 
    for j in range(4)] 
    for i in range(player)]
    for x in range(player)]

# 推理データの表示
for i in range(player):
    print("\n",chr(ord('A')+i))
    for j in range(player):
        print(chr(ord('A')+j),"：",inference[i][j])