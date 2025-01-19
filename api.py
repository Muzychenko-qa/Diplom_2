import urls
import requests
import allure

class StellarburgersAPI:
    @staticmethod
    @allure.step("Создание пользователя")
    def creat_user(body):
        return requests.post(urls.Base_url + urls.Creat_user, json=body)

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(body):
        return requests.post(urls.Base_url + urls.Login_user, data=body)

    @staticmethod
    @allure.step("Изменение данных пользователя")
    def update_user_info(headers, body):
        return requests.patch(urls.Base_url + urls.Changes_user, headers=headers, json=body)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(headers):
        return requests.delete(urls.Base_url + urls.Delete_user, headers=headers)

    @staticmethod
    @allure.step("Создание заказа")
    def creat_order(headers, body):
        return requests.post(urls.Base_url + urls.Creat_order, headers=headers, json=body)

    @staticmethod
    @allure.step("Получение заказа пользователя")
    def receiving_order_user(headers):
        return requests.get(urls.Base_url + urls.Receiving_order_user, headers=headers)

    @staticmethod
    @allure.step("Получение всех заказов")
    def order_all():
        return requests.get(urls.Base_url + urls.Orders_all)

    @staticmethod
    @allure.step("Выход из системы")
    def logout_user(body):
        return requests.post(urls.Base_url + urls.Login_user, json=body)

    @staticmethod
    @allure.step("Обновление токена")
    def refresh_token(body):
        return requests.post(urls.Base_url + urls.Refresh_token, json=body)