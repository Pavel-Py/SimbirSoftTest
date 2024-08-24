import datetime
import os
import time

from hamcrest import assert_that, equal_to, is_
from typing_extensions import TypeIs

from framework.consts import Genders
from framework.page_elements.date_picker import DatePicker

from framework.pages.register_page import RegisterPage
from utils.reports import step, attach


class RegisterSteps:
    _register_page = RegisterPage()

    @classmethod
    def submit_reguister_form(cls, data: dict[str, any]) -> None:
        with step("Заполнить форму регистрации"):
            for field, value in data.items():
                match field:
                    case "firstname":
                        cls._register_page.first_name_input.fill_in(value)
                    case "lastname":
                        cls._register_page.last_name_input.fill_in(value)
                    case "email":
                        cls._register_page.email_input.fill_in(value)
                    case "gender":
                        cls._register_page.get_gender_radio(value).click()
                    case "mobile":
                        cls._register_page.mobile_input.fill_in(value)
                    case "subjects":
                        for subject in value:
                            cls._register_page.subject_input.fill_in(subject)
                            cls._register_page.get_subjects_dropdown_first_item().click()
                    case "hobbies":
                        for hobby in value:
                            cls._register_page.get_hobbies_checkbox(hobby).click()
                    case "picture":
                        cls._register_page.upload_picture_input.fill_in(value)
                    case "birthday":
                        cls._register_page.birthday_button.click()
                        DatePicker().choose_year(str(value.year))
                        DatePicker().choose_month(value.strftime('%B'))
                        DatePicker().choose_day(str(value.day))
                    case "address":
                        cls._register_page.current_address_input.fill_in(value)
                    case "state":
                        cls._register_page.state_button.click()
                        cls._register_page.get_state_dropdown_item(value).click()
                    case "city":
                        cls._register_page.city_button.click()
                        cls._register_page.get_city_dropdown_item(value).click()

    @classmethod
    def send_form(cls) -> None:
        with step("Отправить форму регистрации"):
            cls._register_page.submit_button.click()

    @classmethod
    def check_submitting_form_title(cls, expected_title: str) -> None:
        with step("Проверить, что заголовок заполненной формы соответствует ожидаемому"):
            assert_that(
                cls._register_page.submitting_form_title.get_text(),
                is_(equal_to(expected_title)),
                "Текст не соответствует ожидаемому"
            )

    @classmethod
    def check_submitting_form_data(cls, expected_data: dict[str, any]) -> None:
        with step("Проверить, что данные таблицы соответствуют ожидаемым"):
            expected_table = {
                "Student Name": f"{expected_data['firstname']} {expected_data['lastname']}",
                "Student Email": f"{expected_data['email']}",
                "Gender": f"{expected_data['gender']}",
                "Mobile": f"{expected_data['mobile']}",
                "Date of Birth": expected_data["birthday"].strftime("%d %B,%G"),
                "Subjects": ", ".join(expected_data.get("subjects")),
                "Hobbies": ", ".join(expected_data.get("hobbies")),
                "Address": f"{expected_data['address']}",
                "State and City": f"{expected_data['state']} {expected_data['city']}",
                "Picture": os.path.basename(expected_data['picture'])
            }
            actual_table_data = cls._register_page.get_submitting_form_text_as_dict()
            for actual_title, actual_value in actual_table_data.items():
                attach(f"Актуальный результат '{actual_title}'", actual_value)
                attach("Ожидаемый результат", expected_table[actual_title])
                assert_that(
                    actual_value,
                    is_(equal_to(expected_table[actual_title])),
                    "Данные в заполненой таблице не соответствуют ожидаемым"
                )
