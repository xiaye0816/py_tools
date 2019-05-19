import requests
from py_tools.config import TIAN_API_KEY

api_url = 'http://api.tianapi.com/txapi/finance/?key=%s&code=%s'


def stock_data_query(stock_code):

    stock_data_url = api_url % (TIAN_API_KEY, stock_code)

    stock_data = requests.get(stock_data_url).json()

    return stock_data['newslist']