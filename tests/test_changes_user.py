import allure
from api import StellarburgersAPI
from data import UserData


class TestUpdateUser:

    @allure.title("Изменение данных авторизованного пользователя")
    @allure.description("Тест изменения данных авторизованного пользователя ((email/пароль/имя))")
    def test_update_user_with_auth(self, user_token, delete_user):

        headers = {'Authorization': f'Bearer {user_token}'}

        # Изменяем данные пользователя
        update_user_data = UserData.UPDATE_USER_DATA.copy()
        update_response = StellarburgersAPI.update_user_info(headers, update_user_data)
        print(f"Update response: {update_response.status_code} - {update_response.text}")
        assert update_response.status_code == 200  # Ожидаем успешный статус-код

        # Проверяем, что данные пользователя были успешно изменены
        response_data = update_response.json()
        print(f"Response data: {response_data}")
        assert response_data['user']['email'] == update_user_data["email"]
        assert response_data['user']['name'] == update_user_data["name"]

    @allure.title("Запрос на изменение данных без авторизации")
    @allure.description("Тест получения ошибки 401 на запрос изменения данных без авторизации")
    def test_update_user_without_auth(self, create_user, generate_random_email, delete_user):
        # Создаем нового пользователя
        email = create_user

        # Пытаемся изменить данные пользователя без авторизации
        headers = {}
        update_user_data = UserData.UPDATE_USER_DATA.copy()
        update_response = StellarburgersAPI.update_user_info(headers, update_user_data)
        response_data = update_response.json()
        print(f"Response data: {response_data}")
        assert update_response.status_code == 401
        assert response_data['message'] == 'You should be authorised'
