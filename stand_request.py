import requests
import configuration
import data


# Создание нового заказа
def post_new_orders(user_body):
    req = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=user_body)
    return req


# Получить заказ по его номеру
def post_info_orders(new_track):
    req = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + new_track)
    return req


