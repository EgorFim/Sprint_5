from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from search_elements import TestLocators

class TestKonstruktor:

    def test_bulki(self,driver):
        driver.find_element(*TestLocators.KNOPKA_SOUSY).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.PROVERKA_VKLADKA_SOUSY))
        driver.find_element(*TestLocators.KNOPKA_BULKI).click()
        assert driver.find_element(*TestLocators.PROVERKA_VKLADKA_BULKI)

    def test_sousy(self,driver):
        driver.find_element(*TestLocators.PROVERKA_VKLADKA_BULKI)
        driver.find_element(*TestLocators.KNOPKA_SOUSY).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROVERKA_VKLADKA_SOUSY))
        assert driver.find_element(*TestLocators.PROVERKA_VKLADKA_SOUSY)

    def test_nachinki(self,driver):
        driver.find_element(*TestLocators.PROVERKA_VKLADKA_BULKI)
        driver.find_element(*TestLocators.KNOPKA_NACHINKI).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROVERKA_VKLADKA_NACHINKI))
        assert driver.find_element(*TestLocators.PROVERKA_VKLADKA_NACHINKI)


