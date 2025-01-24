import allure
from api import StellarburgersAPI
from data import *

class TestCreateUser:

    @allure.title("Создание нового пользователя")
    @allure.description("Тест создания/удаления нового пользователя")
    def test_create_user(self, generate_random_email, delete_user):
        email = generate_random_email()
        create_user_data = UserData.CREAT_USER_DATA.copy()
        create_user_data["email"] = email
        request = StellarburgersAPI.creat_user(create_user_data)
        response_data = request.json()
        assert request.status_code == 200 and response_data['success'] is True
        assert response_data['user']['email'] == create_user_data["email"]
        assert response_data['user']['name'] == create_user_data["name"]

    @allure.title("Создание уже зарегистрированного пользователя")
    @allure.description("Тест повторного создния пользователя")
    def test_create_existing_user(self):
        request = StellarburgersAPI.creat_user(UserData.EXISTING_USER_DATA)
        assert request.status_code == 403
        assert request.json() == ResponseData.RESPONSE_DATA_403_1

    @allure.title("Создание пользователя без данных")
    @allure.description("Тест создания пользователя без данных (email/пароль/имя)")
    def test_create_user_blank_data(self):
        request = StellarburgersAPI.creat_user(UserData.BLANK_USER_DATA)
        assert request.status_code == 403
        assert request.json() == ResponseData.RESPONSE_DATA_403_2
