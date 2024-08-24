

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing_extensions import Self

from utils.reports import step


class BaseElement:
    driver: WebDriver = None

    def __init__(self, locator: By, value: str, name: str = None, wait_time: int = 5):
        self.locator = locator if locator else By.XPATH
        self.locator_value = value
        self.name = name
        self.wait_time = wait_time
        self.element: WebElement = self._get_element()

    def _get_element(self) -> WebElement:
        try:
            element = WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((self.locator, self.locator_value))
            )
            if not element.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element
        except TimeoutException:
            raise Exception(f"Элемент не найден за {self.wait_time} секунд")

    def get_child_element(self, extra_locator: str, name: str = None) -> Self:
        return BaseElement(By.XPATH, f"{self.locator_value}{extra_locator}", name=name)

    def get_child_elements(self, extra_locator: str) -> list[Self]:
        amount_elements = self.element.find_elements(By.XPATH, f"{self.locator_value}{extra_locator}").__len__()
        return [
            self.get_child_element(extra_locator=f"{extra_locator}[{num}]")
            for num in range(1, amount_elements + 1)
        ]

    def click(self) -> None:
        with step(f"Кликнуть по элементу {self.name}"):
            ActionChains(self.driver).move_to_element(self.element).click(self.element).perform()

    def fill_in(self, text: str) -> None:
        with step(f"Заполнить поле {self.name} текстом {text}"):
            self.element.send_keys(text)

    def get_text(self) -> str:
        with step(f"Получить текст элемента {self.name}"):
            return self.element.text
