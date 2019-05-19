import os
import configparser

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("py_tools")+len("py_tools")]

config = configparser.ConfigParser()
config.read(rootPath + '/.env')

section_default = config['default']
section_ding_talk = config['ding_talk']
section_tian_api = config['tian_api']

APPLICATION_NAME = section_default['application_name']

DING_TALK_ROBOT_ACCESS_TOKEN = section_ding_talk['robot_access_token']

TIAN_API_KEY = section_tian_api['api_key']

__all__ = [
    'APPLICATION_NAME',
    'DING_TALK_ROBOT_ACCESS_TOKEN',
    'TIAN_API_KEY'
]