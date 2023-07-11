import data
import stand_request

# Проверка получения данных о заказе по треку заказа

def test_get_info():
    order_response = stand_request.post_new_orders(data.user_body)
    assert order_response.status_code == 201
    new_track = str(order_response.json()['track'])
    info_response = stand_request.post_info_orders(new_track)
    assert info_response.status_code == 200

