import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from framework.consts import Urls
from steps.base_step import BaseStep

from framework.page_elements.base_element import BaseElement


@pytest.fixture
def driver_init():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'none'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    BaseElement.driver = driver
    yield driver
    driver.quit()


@pytest.fixture()
def open_main(driver_init):
    BaseStep.open(driver_init, Urls.START_URI)

