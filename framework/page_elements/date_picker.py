from selenium.webdriver.common.by import By

from framework.page_elements.base_element import BaseElement
from utils.reports import step


class DatePicker:
    @property
    def year_button(self) -> BaseElement:
        return BaseElement(By.XPATH, "//select[@class='react-datepicker__year-select']", name="Year button")

    @property
    def month_button(self) -> BaseElement:
        return BaseElement(By.XPATH, "//select[@class='react-datepicker__month-select']", name="month button")

    @property
    def days_window(self):
        return BaseElement(By.XPATH, "//div[@class='react-datepicker__month']")

    def choose_year(self, year: str) -> None:
        with step(f"Выбрать {year} год"):
            self.year_button.click()
            self.year_button.element.send_keys("1987")
            self.year_button.click()

    def choose_month(self, month: str) -> None:
        with step(f"Выбрать месяц {month}"):
            self.month_button.click()
            self.month_button.element.send_keys(month)
            self.month_button.click()

    def choose_day(self, day: str) -> None:
        with step(f"Выбрать день - {day}"):
            self.days_window.get_child_element(
                f"//div[not(contains(@class, 'outside')) and text()='{day}']", name=f"Day {day}"
            ).click()
