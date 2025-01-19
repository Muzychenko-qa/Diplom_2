import random
class UserData:

    DEFAULT_PASSWORD = "Pass0896"
    DEFAULT_NAME = "Ptrenko Petro"

    CREAT_USER_DATA = {
        "password": DEFAULT_PASSWORD,
        "name": DEFAULT_NAME
    }

    BLANK_USER_DATA = {
        "email": "",
        "password": "",
        "name": ""
    }

    EXISTING_USER_DATA = {
        "email": "test001@yandex.ru",
        "password": DEFAULT_PASSWORD,
        "name": DEFAULT_NAME
    }

    INCORRECT_LOGIN_DATA = {
        "email": "test001@yAnbex.du",
        "password": "Bass0686"
    }

    # Данные для обновления пользователя с использованием random.randint
    UPDATE_USER_DATA = {
        "email": f"{random.randint(1, 999)}beard@vghux.ru",
        "password": f"new_password{random.randint(1000, 9999)}",
        "name": f"New Name {random.randint(1, 999)}"
    }

class OrderData:


    INGREDIENT_1 = "61c0c5a71d1f82001bdaaa7a"
    INGREDIENT_2 = "61c0c5a71d1f82001bdaaa79"
    INGREDIENT_3 = "61c0c5a71d1f82001bdaaa71"
    INGREDIENT_4 = "61c0c5a71d1f82001bdaaa6f"
    INGREDIENT_5 = "61c0c5a71d1f82001bdaaa70"
    INGREDIENT_6 = "61c0c5a71d1f82001bdaaa75"
    WRONG_INGREDIENT = "61c9c5a71d1f82001bdaAa75"
    EMPTY_INGREDIENT = ""


    ONE_ORDER_INGREDIENTS = {
        "ingredients": [INGREDIENT_1]
    }

    MANY_ORDER_INGREDIENTS = {
        "ingredients": [INGREDIENT_3, INGREDIENT_2, INGREDIENT_5, INGREDIENT_1, INGREDIENT_4]
    }

    WRONG_ORDER_INGREDIENTS = {
        "ingredients": [WRONG_INGREDIENT]
    }

    WRONG_ORDER_INGREDIENTS_2 = {
        "ingredients": [EMPTY_INGREDIENT]
    }