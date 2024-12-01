import requests
from pprint import pprint


def get_digikala_plp(plp):
    response = None
    try:
        response = requests.get(f"https://api.digikala.com/v1/promotions/plp_{plp}/")
        pprint(response.json())

    except:
        pprint(response.status_code)
        pprint("can not fetch plps")


def get_users_posts():
    response = None
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        pprint(response.json())

    except:
        pprint(response.status_code)
        pprint("can not fetch plps")


get_digikala_plp("216294622")

get_users_posts()
