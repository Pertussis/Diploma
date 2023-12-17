# Антонина Акименко, 11-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_create_and_get_order():
    # Создаем новый заказ
    sender_stand_request.post_new_order(data.order_body)
    # Получаем трек-номер заказа
    sender_stand_request.get_new_order_track()
    # Отправляем запрос на получение заказа по трек-номеру
    sender_stand_request.get_order()
    # Проверяем, что статус ответа 200
    assert sender_stand_request.get_order().status_code == 200
    # Печатаем тело ответа, содержащие данные о нашем заказе
    print(sender_stand_request.get_order().json())
