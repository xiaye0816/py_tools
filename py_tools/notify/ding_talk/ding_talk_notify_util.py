import requests
from py_tools.config import DING_TALK_ROBOT_ACCESS_TOKEN
from py_tools.config import DING_TALK_RISHANG_ROBOT_ACCESS_TOKEN


def send_robot_notify(notify_text):

    url = "https://oapi.dingtalk.com/robot/send"

    querystring = {"access_token": DING_TALK_ROBOT_ACCESS_TOKEN}

    payload = "{'msgtype':'text','text':{'content':'%s'}}" % notify_text

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
    }

    print("ready send to ding talk notify:" + notify_text)

    response = requests.request("POST", url, data=payload.encode(), headers=headers, params=querystring)

    print("response:" + response.text)


def send_rishang_robot_notify(notify_text):

    url = "https://oapi.dingtalk.com/robot/send"

    querystring = {"access_token": DING_TALK_RISHANG_ROBOT_ACCESS_TOKEN}

    payload = "{'msgtype':'text','text':{'content':'%s'}, 'at':{'isAtAll':true}}" % notify_text

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
    }

    print("ready send to ding talk notify:" + notify_text)

    response = requests.request("POST", url, data=payload.encode(), headers=headers, params=querystring)

    print("response:" + response.text)