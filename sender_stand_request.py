import configuration
import requests
import data


def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body,
                         headers=data.headers)


response = post_new_order(data.order_body)
print(response.json())


def get_new_order_track():
    new_track = response.json().get("track")

    return new_track


def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_PATH,
                        params={"t": get_new_order_track()})
