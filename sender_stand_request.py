import configuration
import requests
import data

# Функция для создания нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body,
                         headers=data.headers)


# Функция для получения заказа по трек-номеру
def get_new_order_track(new_track):
    return requests.get(f"{configuration.URL_SERVICE}/api/v1/orders/track?t={new_track}")
