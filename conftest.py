import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from search_elements import TestLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ZAGRUZKA_GLAVNOI))
    yield driver
    driver.quit()

@pytest.fixture
def driver_2():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.ZAGRUZKA_GLAVNOI))
    driver.find_element(*TestLocators.KNOPKA_LICHNYI_KABINET).click()
    driver.find_element(*TestLocators.EMAIL_ADD).send_keys("egorfimushkin11137@yandex.ru")
    driver.find_element(*TestLocators.PASSWORD_ADD).send_keys("123456")
    driver.find_element(*TestLocators.VOITY_BUTTON_AFTER_ADD).click()
    yield driver
    driver.quit()

