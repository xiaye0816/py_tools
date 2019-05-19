from py_tools.data.movie import movie_util
from py_tools.notify.ding_talk import ding_talk_notify_util
import time


movie_id = 344328
movie_name = "X战警：黑凤凰"

# movie_id = 248172
# movie_name = "复仇者联盟4：终局之战"

while True:

    open_booking = movie_util.check_movie_open_booking(movie_id)

    if open_booking:
        print("[%s]开始预售啦~" % movie_name)
        ding_talk_notify_util.send_robot_notify("[%s]开始预售啦~" % movie_name)
        break
    else:
        print("[%s]预售尚未开启...5秒后重试..." % movie_name)
        time.sleep(5)