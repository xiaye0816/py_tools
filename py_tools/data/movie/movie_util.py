import requests

maoyan_url = "https://maoyan.com/films/%s"


def check_movie_open_booking(maoyan_movie_id):

    url = maoyan_url % maoyan_movie_id

    html = requests.get(url).text

    start_pre_sell = html.find("特惠购票") > -1

    return start_pre_sell
