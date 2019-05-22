from py_tools.data.stock import stock_data_util
from py_tools.notify.ding_talk import ding_talk_notify_util
import time

# stock_code = 'sh600794'
stock_code = 'sh601018'

notified_percent_level = None

current_percent_level = None

notify_text = '[%s] 当前:%s 基础:%s 涨跌幅:[%s%%]'

fast_check_count = 0

while True:

    stock_data = stock_data_util.stock_data_query(stock_code)

    stock_name = stock_data[0]
    base_price = float(stock_data[2])
    current_price = float(stock_data[3])

    print("stock_name %s current_price:%s" % (stock_name, current_price))

    current_percent_level = int((current_price - base_price) / base_price * 100)

    if current_percent_level != notified_percent_level:
        ding_talk_notify_util.send_robot_notify(
            notify_text % (stock_name, current_price, base_price, round((current_price - base_price) / base_price * 100, 2)))
        notified_percent_level = current_percent_level
        fast_check_count = 5

    if fast_check_count > 0:
        time.sleep(1)
        fast_check_count = fast_check_count - 1
    else:
        time.sleep(5)