from selenium.webdriver.common.by import By
from typing_extensions import TypeIs

from framework.consts import Genders
from framework.page_elements.base_element import BaseElement
from framework.pages.base_page import BasePage


class RegisterPage(BasePage):
    @property
    def first_name_input(self) -> BaseElement:
        return BaseElement(By.ID, "firstName", name="First name input")

    @property
    def last_name_input(self) -> BaseElement:
        return BaseElement(By.ID, "lastName", name="Last name input")

    @property
    def email_input(self) -> BaseElement:
        return BaseElement(By.ID, "userEmail", name="Email input")

    @property
    def mobile_input(self) -> BaseElement:
        return BaseElement(By.ID, "userNumber", name="Mobile input")

    @property
    def date_of_births_input(self) -> BaseElement:
        return BaseElement(By.ID, "dateOfBirthInput", name="Date of births input")

    @property
    def subject_input(self) -> BaseElement:
        return BaseElement(By.ID, "subjectsInput", name="Subject input")

    @property
    def subjects_dropdown(self) -> BaseElement:
        return BaseElement(By.XPATH, "//div[contains(@class,'subjects-auto-complete__menu')]")

    def get_subjects_dropdown_first_item(self) -> BaseElement:
        return self.subjects_dropdown.get_child_element(
            "//div[@id='react-select-2-option-0']", name="first dropdown item"
        )

    @property
    def current_address_input(self) -> BaseElement:
        return BaseElement(By.ID, "currentAddress", name="Current address input")

    @staticmethod
    def get_gender_radio(value: TypeIs[Genders]) -> BaseElement:
        genders = {
            Genders.MALE: BaseElement(By.CSS_SELECTOR, "input[value=Male]", name="male gender radio"),
            Genders.FEMALE: BaseElement(By.CSS_SELECTOR, "input[value=Female]", name="female gender radio"),
            Genders.OTHER: BaseElement(By.CSS_SELECTOR, "input[value=Other]", name="other gender radio"),
        }
        return genders.get(value)

    @property
    def birthday_button(self):
        return BaseElement(By.XPATH, "//div[@class='react-datepicker-wrapper']")

    @staticmethod
    def get_hobbies_checkbox(value: str) -> BaseElement:
        return BaseElement(By.XPATH, f"//label[contains(text(), '{value}')]")

    @property
    def upload_picture_input(self) -> BaseElement:
        return BaseElement(By.XPATH, "//input[@id='uploadPicture']", name="picture uploader")

    @property
    def state_button(self) -> BaseElement:
        return BaseElement(By.XPATH, "//div[@id='stateCity-wrapper']//div[@id='state']", name="state button")

    @staticmethod
    def get_state_dropdown_item(text) -> BaseElement:
        return BaseElement(
            By.XPATH,
            f"//div[@id='state']//div[contains(@id, 'react-select-3') and text()='{text}']",
            name=f"state dropdown item '{text}'"
        )

    @property
    def city_button(self) -> BaseElement:
        return BaseElement(By.XPATH, "//div[@id='stateCity-wrapper']//div[@id='city']", name="city button")

    @staticmethod
    def get_city_dropdown_item(text) -> BaseElement:
        return BaseElement(
            By.XPATH,
            f"//div[@id='city']//div[contains(@id, 'react-select-4') and text()='{text}']",
            name=f"city dropdown item '{text}'"
        )

    @property
    def submit_button(self) -> BaseElement:
        return BaseElement(By.XPATH, "//button[@id='submit']", name="submit button")

    @property
    def submitting_form_title(self) -> BaseElement:
        return BaseElement(By.XPATH, "//div[contains(@class, 'modal-title')]")

    @property
    def submitting_form(self) -> BaseElement:
        return BaseElement(By.XPATH, "//div[@class='table-responsive']//tbody", name="submiting form")

    def get_submitting_form_text_as_dict(self) -> dict[str, str]:
        tr_list = self.submitting_form.get_child_elements("//tr")
        table_as_dict = {}
        for item in tr_list:
            lable, value = item.get_child_elements("//td")
            table_as_dict[lable.get_text()] = value.get_text()
        return table_as_dict
