from py_tools.config import APPLICATION_NAME
from py_tools.config import DING_TALK_ROBOT_ACCESS_TOKEN
from py_tools.config import TIAN_API_KEY

from py_tools.notify.ding_talk import ding_talk_notify_util
from py_tools.data.stock import stock_data_util
from py_tools.data.movie import movie_util

print(APPLICATION_NAME)
print(DING_TALK_ROBOT_ACCESS_TOKEN)
print(TIAN_API_KEY)
ding_talk_notify_util.send_robot_notify('哈哈')
# print(stock_data_util.stock_data_query('hk00700'))
# print(movie_util.check_movie_open_booking(1280791))