import os
import configparser

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("py_tools")+len("py_tools")]

config = configparser.ConfigParser()
config.read(rootPath + '/.env')

section_default = config['default']
section_ding_talk = config['ding_talk']
section_tian_api = config['tian_api']
section_rishang = config['rishang']

APPLICATION_NAME = section_default['application_name']

DING_TALK_ROBOT_ACCESS_TOKEN = section_ding_talk['robot_access_token']
DING_TALK_RISHANG_ROBOT_ACCESS_TOKEN = section_ding_talk['rishang_robot_access_token']

TIAN_API_KEY = section_tian_api['api_key']

RISHANG_TOKEN = section_rishang['rishang_token']

__all__ = [
    'APPLICATION_NAME',
    'DING_TALK_ROBOT_ACCESS_TOKEN',
    'DING_TALK_RISHANG_ROBOT_ACCESS_TOKEN',
    'TIAN_API_KEY',
    'RISHANG_TOKEN'
]