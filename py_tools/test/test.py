from py_tools.config import APPLICATION_NAME
from py_tools.config import DING_TALK_ROBOT_ACCESS_TOKEN
from py_tools.notify.ding_talk import ding_talk_notify_util


print(APPLICATION_NAME)
print(DING_TALK_ROBOT_ACCESS_TOKEN)
ding_talk_notify_util.send_robot_notify('1234569')