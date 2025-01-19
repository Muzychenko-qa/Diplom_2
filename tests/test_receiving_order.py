import allure
from api import StellarburgersAPI
from data import OrderData


class TestReceivingOrderUser:

    @allure.title("Получение заказов пользователя")
    @allure.description("Тест получения заказов пользователя (с авторизацией)")
    def test_receiving_order_authorized_user(self, user_token, delete_user):
        headers = {'Authorization': f'Bearer {user_token}'}

        # Создание заказа
        order_response = StellarburgersAPI.creat_order(headers, OrderData.ONE_ORDER_INGREDIENTS)
        assert order_response.status_code == 200

        # Получаем заказы пользователя
        receiving_response = StellarburgersAPI.receiving_order_user(headers)
        response_data = receiving_response.json()
        print(f"Response data: {response_data}")
        assert receiving_response.status_code == 200
        assert response_data['orders'][0]['name'] == 'Астероидный бургер'

    @allure.title("Получение заказов пользователя")
    @allure.description("Тест получения заказов пользователя (без авторизации)")
    def test_receiving_order_user_without_auth(self):

        headers = {}
        order_response = StellarburgersAPI.receiving_order_user(headers)
        response_data = order_response.json()
        print(f"Response data: {response_data}")
        assert order_response.status_code == 401
        assert response_data['message'] == 'You should be authorised'
