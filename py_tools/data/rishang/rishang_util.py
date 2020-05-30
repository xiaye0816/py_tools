import requests
from py_tools.notify.ding_talk import ding_talk_notify_util
from py_tools.config import RISHANG_TOKEN
import time
import datetime

rishang_url = "https://mbff.yuegowu.com/site/purchases"

def check_rishang_stock(goodsId):

    header = {"Authorization": RISHANG_TOKEN, "Content-Type":"application/json"}

    try:
        json = requests.post(rishang_url, data='{"goodsInfoIds":[]}', headers=header).json()

        goods_list = json['context']['goodsInfos']

        for goods in goods_list:
            if goods['goodsId'] == goodsId:
                goodsInfoName = goods['goodsInfoName']
                goodsStatus = goods['goodsStatus']
                salePrice = goods['salePrice']

                notify_text = goodsInfoName + "，价格：" + str(salePrice) + "，当前库存状态："
                if goodsStatus == 0:
                    notify_text += "有库存啦！！"
                    ding_talk_notify_util.send_rishang_robot_notify(notify_text)
                    raise Exception("结束查询")
                else:
                    notify_text += "还没有库存哦..." + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(notify_text)
                    time.sleep(5)

    except:
        ding_talk_notify_util.send_rishang_robot_notify("查询库存失败啦，小哥哥快去检查一下!")
        raise





