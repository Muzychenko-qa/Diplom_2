import allure
from api import StellarburgersAPI
from data import *


class TestCreatOrder:

    @allure.title("Создание заказа с авторизацией")
    @allure.description("Тест создания заказа авторизованным пользователем")
    def test_creat_order_authorized_user(self, user_token, delete_user):
        headers = {'Authorization': f'Bearer {user_token}'}
        order_response = StellarburgersAPI.creat_order(headers, OrderData.ONE_ORDER_INGREDIENTS)
        response_data = order_response.json()
        print(f"Response data: {response_data}")
        assert order_response.status_code == 200 and response_data['success'] is True
        assert response_data['name'] == 'Астероидный бургер'

    @allure.title("Создание заказа без авторизации")
    @allure.description("Тест создания заказа без авторизации")
    def test_creat_order_not_authorized_user(self):
        headers = {}
        order_response = StellarburgersAPI.creat_order(headers, OrderData.MANY_ORDER_INGREDIENTS)
        response_data = order_response.json()
        print(f"Response data: {response_data}")
        assert order_response.status_code == 200 and response_data['success'] is True
        assert response_data['name'] == 'Экзо-плантаго метеоритный бессмертный био-марсианский астероидный бургер'

    @allure.title("Создание заказа c неверным хэшем ингредиентов")
    @allure.description("Тест создания заказа c неверным хэшем ингредиентов (с авторизацией)")
    def test_creat_order_wrong_ingredients(self, user_token, delete_user):
        headers = {'Authorization': f'Bearer {user_token}'}
        order_response = StellarburgersAPI.creat_order(headers, OrderData.WRONG_ORDER_INGREDIENTS)
        response_data = order_response.json()
        print(f"Response data: {response_data}")
        assert order_response.status_code == 400 and response_data['success'] is False
        assert response_data == ResponseData.RESPONSE_DATA_400_1

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Тест создания заказа без ингредиентов (без авторизации)")
    def test_creat_order_not_ingredients(self):
        headers = {}
        order_response = StellarburgersAPI.creat_order(headers, OrderData.WRONG_ORDER_INGREDIENTS_2)
        assert order_response.status_code == 500
        response_text = order_response.text
        assert "Internal Server Error" in response_text
