# werewolf
**概要**：[プログラム設計法 -glegle-](https://hackmd.io/leij7JgrQ0mpkJi3wUoPuQ?view)  

## ディレクトリ構造
```
werewolf
│  readme.md
│
├─python
│  │  pip.txt
│  │
│  ├─agent
│  │      agent_action_func.py
│  │      agent_deduce_func.py
│  │      agent_vote_func.py
│  │      template.py
│  │
│  ├─main
│  │      night_func.py
│  │      noon_func.py
│  │      start_night_func.py
│  │      start_noon_func.py
│  │      vote_func.py
│  │
│  └─set
│          end_func.py
│          restart_func.py
│          select_func.py
│          start_func.py
│
└─test
    │  job_distribution.py
    │  slack_get_test.py
    │  slack_test.py
    │
    └─demo
            main.py
```