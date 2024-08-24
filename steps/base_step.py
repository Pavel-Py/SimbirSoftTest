from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from framework.page_elements.base_element import BaseElement


class BaseStep:
    @classmethod
    def open(cls, driver: WebDriver, url: str):
        driver.get(url)
