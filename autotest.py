# Антонина Акименко, 11-я когорта - Финальный проект. Инженер по тестированию плюс.

import data
import sender_stand_request


def test_create_and_get_order():
    # Создаем новый заказ
    response = sender_stand_request.post_new_order(data.order_body)
    # Получаем трек-номер заказа
    new_track = response.json().get("track")
    # Отправляем запрос на получение заказа по трек-номеру
    sender_stand_request.get_new_order_track(new_track)
    # Проверяем, что статус ответа 200
    assert sender_stand_request.get_new_order_track(new_track).status_code == 200
