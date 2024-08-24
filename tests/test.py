import datetime
import os

import allure

from framework.consts import Genders
from steps.register_steps import RegisterSteps


@allure.suite("Форма регистрации")
class TestRegister:

    @allure.title("Проверка отправки формы с корректно заполненными полями")
    def test_successful_filling_register_form(self, open_main):
        data_to_submit = {
            "firstname": "test firstname",
            "lastname": "test lastmane",
            "email": "email@mail.com",
            "gender": Genders.MALE,
            "mobile": "8005553535",
            "birthday": datetime.date(1987, 11, 12),
            "subjects": ("Maths", "Physics"),
            "hobbies": ("Sports", "Reading"),
            "picture": os.path.join(os.getcwd(), "test_data", "test_picture.jpg"),
            "address": "test street 11",
            "state": "Haryana",
            "city": "Karnal",
        }
        exp_title = "Thanks for submitting the form"
        RegisterSteps.submit_reguister_form(data_to_submit)
        RegisterSteps.send_form()
        RegisterSteps.check_submitting_form_title(expected_title=exp_title)
        RegisterSteps.check_submitting_form_data(data_to_submit)
