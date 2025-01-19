import allure
from api import StellarburgersAPI
from data import UserData

class TestLoginUser:

    @allure.title("Авторизация пользователя")
    @allure.description("Тест авторизации нового пользователя")
    def test_login_user(self, generate_random_email, delete_user):

        # Создаем нового пользователя
        email = generate_random_email()
        create_user_data = UserData.CREAT_USER_DATA.copy()
        create_user_data["email"] = email
        create_response = StellarburgersAPI.creat_user(create_user_data)
        assert create_response.status_code == 200

        # Логинимся и проверяем успешный ответ
        login_data = {"email": email, "password": UserData.DEFAULT_PASSWORD}
        request = StellarburgersAPI.login_user(login_data)
        response_data = request.json()
        print(f"Response data: {response_data}")
        assert request.status_code == 200
        assert response_data['user']['email'] == create_user_data["email"]
        assert response_data['user']['name'] == create_user_data["name"]

    @allure.title("Передача некорректных данных при авторизации")
    @allure.description("Тест авторизации с некорретными данными")
    def test_login_user_incorrect_data(self):
        request = StellarburgersAPI.login_user(UserData.INCORRECT_LOGIN_DATA)
        assert request.status_code == 401
        assert request.json() == {"success": False, "message": "email or password are incorrect"}