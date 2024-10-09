from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from search_elements import TestLocators



class TestRegistration:

    def test_registration_successful(self,driver):

        driver.find_element(*TestLocators.VOITY_BUTTON).click()
        driver.find_element(*TestLocators.REGISTER_BUTTON_1).click()


        driver.find_element(*TestLocators.NAME_INPUT_FIELD).send_keys('Егор')
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys("egorfimushkin11137@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys('123456')
        driver.find_element(*TestLocators.REGISTER_BUTTON_FINAL).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.OZHIDANIE_POSLE_ZAPOLNENIYA_REGISTRACII))
        driver.find_element(*TestLocators.EMAIL_ADD).send_keys("egorfimushkin11137@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_ADD).send_keys("123456")
        driver.find_element(*TestLocators.VOITY_BUTTON_AFTER_ADD).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(TestLocators.PROVERKA_USPESHNOGO_VHODA))
        assert driver.find_element(*TestLocators.PROVERKA_USPESHNOGO_VHODA)


    def test_registration_non_valid_password(self,driver):

        driver.find_element(*TestLocators.VOITY_BUTTON).click()
        driver.find_element(*TestLocators.REGISTER_BUTTON_1).click()

        driver.find_element(*TestLocators.NAME_INPUT_FIELD).send_keys('Егор')
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys("egorfimushkin11126@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys('12345')
        driver.find_element(*TestLocators.REGISTER_BUTTON_FINAL).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.NEVERNIY_PAROL))
        assert driver.find_element(*TestLocators.NEVERNIY_PAROL)





