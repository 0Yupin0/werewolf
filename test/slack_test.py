# slack接続用
import requests     # pip install requests
import json

# slack接続定義
WEB_HOOK_URL = "https://hooks.slack.com/services/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"
message="てすとてすとてすと"

requests.post(WEB_HOOK_URL, data=json.dumps({
    "channel" : "#人狼テスト",
    "text" : message,
    "icon_emoji" : ":pizza:",
    "username" : "system"
}))