import random
import string
import pytest
import allure
from api import StellarburgersAPI
from data import UserData

@pytest.fixture(scope="session")
@allure.step("Генерация случайного email пользователя")
def generate_random_email():
    def _generate_email():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(6))
        domain = ''.join(random.choice(letters) for i in range(5))
        email = f"{random_string}@{domain}.com"
        return email
    return _generate_email

@pytest.fixture(scope="function")
@allure.step("Создание нового пользователя")
def create_user(generate_random_email):
    email = generate_random_email()
    user_data = UserData.CREAT_USER_DATA.copy()
    user_data["email"] = email
    response = StellarburgersAPI.creat_user(user_data)
    assert response.status_code == 200
    return email

@pytest.fixture(scope="function")
@allure.step("Токен пользоватея")
def user_token(create_user):
    email = create_user
    login_data = {"email": email, "password": UserData.DEFAULT_PASSWORD}
    login_response = StellarburgersAPI.login_user(login_data)
    token = login_response.json().get("accessToken").replace("Bearer ", "")
    assert token is not None
    return token

@pytest.fixture(scope="function")
@allure.step("Удаление пользователя")
def delete_user(create_user, user_token):
    email = create_user
    headers = {'Authorization': f'Bearer {user_token}'}
    yield
    StellarburgersAPI.delete_user(headers)