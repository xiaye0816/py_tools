from py_tools.data.stock import stock_data_util
from py_tools.notify.ding_talk import ding_talk_notify_util
import time


def func():
    # 股票代码
    stock_code = 'sh600794'
    # stock_code = 'sh601018'

    # 已通知percent 按百分比取整
    notified_percent_level = None

    # 当前percent 按百分比取整
    current_percent_level = None

    # 当前价格
    notified_price = None

    notify_text = '[%s] 当前:%s 基础:%s 涨跌幅:[%s%%]'

    # 快速查询剩余次数 (每次触发percent变化后, 每秒查询一次, 连续5次，其他时间每5秒查询一次)
    fast_check_count = 0

    while True:

        try:
            # 查询实时数据
            stock_data = stock_data_util.stock_data_query(stock_code)

            print(stock_data)

            stock_name = stock_data[0]
            base_price = float(stock_data[2])
            current_price = float(stock_data[3])

            print("stock_name %s current_price:%s" % (stock_name, current_price))

            # 计算当前percent level 按百分比取整
            current_percent_level = int((current_price - base_price) / base_price * 100)

            # 如果current_percent_level发生变化 触发通知
            if current_percent_level != notified_percent_level:

                # 发送通知
                ding_talk_notify_util.send_robot_notify(
                    notify_text % (
                        stock_name, current_price, base_price,
                        round((current_price - base_price) / base_price * 100, 2)))

                # 防止一分钱拉锯导致连续通知
                if notified_price and abs(notified_price - current_price) > 0.01:
                    fast_check_count = 5

                notified_price = current_price
                notified_percent_level = current_percent_level

        except:
            print("查询出错了...")

        # 休息片刻，重新拉取数据
        if fast_check_count > 0:
            time.sleep(1)
            fast_check_count = fast_check_count - 1
        else:
            time.sleep(10)


if __name__ == '__main__':
    func()
