from py_tools.data.stock import stock_data_util
from py_tools.notify.ding_talk import ding_talk_notify_util
import time
import datetime


def func():

    # 股票代码
    stock_code = 'sz002916'
    # stock_code = 'sz000089'
    # stock_code = 'sh603817'

    notified_price = None

    trigger_notify_price = 0.5

    notify_text = '[%s] 当前:%s 基础:%s 涨跌幅:[%s%%]'

    fast_check_count = 0

    while True:

        if datetime.datetime.now().hour < 9 or datetime.datetime.now().hour >= 15 or datetime.datetime.now() == 12:
            print("超出交易时间，本次不调API查询，continue..." + str(datetime.datetime.now()))
        else:
            try:

                # 查询实时数据
                stock_data = stock_data_util.stock_data_query(stock_code)

                stock_name = stock_data[0]
                base_price = float(stock_data[2])
                current_price = float(stock_data[3])

                print("%s 当前: %s" % (stock_name, current_price))

                if not notified_price or abs(current_price - notified_price) >= trigger_notify_price:
                    notified_price = current_price
                    # trigger_notify_price = base_price / 10

                    ding_talk_notify_util.send_robot_notify(
                        notify_text % (
                            stock_name, current_price, base_price,
                            round((current_price - base_price) / base_price * 100, 2)))

                    fast_check_count = 3

            except:

                print("查询出错了...")

        if fast_check_count > 0:
            time.sleep(3)
            fast_check_count -= 1
        else:
            time.sleep(10)

if __name__ == '__main__':
    func()
