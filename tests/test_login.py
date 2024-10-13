from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from search_elements import TestLocators


class TestLogin:

    def test_login_from_main_on_button_voitivakkaunt(self,driver):
        driver.find_element(*TestLocators.VOITY_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_ADD).send_keys("egorfimushkin11119@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_ADD).send_keys("123456")
        driver.find_element(*TestLocators.VOITY_BUTTON_AFTER_ADD).click()
        assert WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.PROVERKA_USPESHNOGO_VHODA))


    def test_login_from_button_lichnyi_kabinet(self,driver):
        driver.find_element(*TestLocators.KNOPKA_LICHNYI_KABINET).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.EMAIL_ADD))
        driver.find_element(*TestLocators.EMAIL_ADD).send_keys("egorfimushkin11119@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_ADD).send_keys("123456")
        driver.find_element(*TestLocators.VOITY_BUTTON_AFTER_ADD).click()
        assert WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.PROVERKA_USPESHNOGO_VHODA))

    def test_login_from_forma_registracii(self,driver):
        driver.find_element(*TestLocators.VOITY_BUTTON).click()
        driver.find_element(*TestLocators.REGISTER_BUTTON_1).click()
        driver.find_element(*TestLocators.VOITY_IZ_OKNA_REGISTRACII).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.EMAIL_ADD))
        driver.find_element(*TestLocators.EMAIL_ADD).send_keys("egorfimushkin11119@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_ADD).send_keys("123456")
        driver.find_element(*TestLocators.VOITY_BUTTON_AFTER_ADD).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROVERKA_USPESHNOGO_VHODA))

    def test_login_from_forma_vosstanovl_parol(self,driver):
        driver.find_element(*TestLocators.VOITY_BUTTON).click()
        driver.find_element(*TestLocators.KNOPKA_VOSSTANOVIT_PAROL).click()
        driver.find_element(*TestLocators.VOITY_IZ_OKNA_REGISTRACII).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.EMAIL_ADD))
        driver.find_element(*TestLocators.EMAIL_ADD).send_keys("egorfimushkin11119@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_ADD).send_keys("123456")
        driver.find_element(*TestLocators.VOITY_BUTTON_AFTER_ADD).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PROVERKA_USPESHNOGO_VHODA))

