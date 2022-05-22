import requests

import config_private as priv


def send_message(txt, token = priv.token_telegram, chat_id = priv.chat_id_telegram):
    url_api = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="+ str(txt)
    resp = requests.get(url_api)
    print(resp.content)
    print(resp.json())


#telegram_message(token, txt, bot_channel)