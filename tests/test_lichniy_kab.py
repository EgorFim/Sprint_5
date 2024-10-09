from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from search_elements import TestLocators

class TestLichnyiKabinet:

    def test_vhoda_v_lichnyi_po_knopke(self,driver_2):
        WebDriverWait(driver_2,3).until(expected_conditions.visibility_of_element_located(TestLocators.KNOPKA_LICHNYI_KABINET))
        driver_2.find_element(*TestLocators.KNOPKA_LICHNYI_KABINET).click()
        WebDriverWait(driver_2,3).until(expected_conditions.visibility_of_element_located(TestLocators.V_LICHNOM_KABINETE))
        assert '/account/profile' in driver_2.current_url

    def test_perehod_v_konstruktor_po_kliku_iz_kabineta(self,driver_2):
        WebDriverWait(driver_2, 3).until(expected_conditions.visibility_of_element_located(TestLocators.KNOPKA_LICHNYI_KABINET))
        driver_2.find_element(*TestLocators.KNOPKA_LICHNYI_KABINET).click()
        WebDriverWait(driver_2, 3).until(expected_conditions.visibility_of_element_located(TestLocators.V_LICHNOM_KABINETE))
        driver_2.find_element(*TestLocators.KNOPKA_KONSTRUKTOR).click()
        assert WebDriverWait(driver_2,3).until(expected_conditions.visibility_of_element_located(TestLocators.KONSTRUKTOR_PROVERKA))

    def test_perehod_v_konstruktor_po_stellar_burgers(self,driver_2):
        WebDriverWait(driver_2, 3).until(expected_conditions.visibility_of_element_located(TestLocators.KNOPKA_LICHNYI_KABINET))
        driver_2.find_element(*TestLocators.KNOPKA_LICHNYI_KABINET).click()
        WebDriverWait(driver_2, 3).until(expected_conditions.visibility_of_element_located(TestLocators.V_LICHNOM_KABINETE))
        driver_2.find_element(*TestLocators.KNOPKA_STELLAR).click()
        assert WebDriverWait(driver_2, 3).until(expected_conditions.visibility_of_element_located(TestLocators.KONSTRUKTOR_PROVERKA))

    def test_vyhod_iz_kabineta(self,driver_2):
        WebDriverWait(driver_2, 3).until(expected_conditions.visibility_of_element_located(TestLocators.KNOPKA_LICHNYI_KABINET))
        driver_2.find_element(*TestLocators.KNOPKA_LICHNYI_KABINET).click()
        WebDriverWait(driver_2, 3).until(expected_conditions.visibility_of_element_located(TestLocators.V_LICHNOM_KABINETE))
        driver_2.find_element(*TestLocators.KNOPKA_VYHOD).click()
        assert WebDriverWait(driver_2, 3).until(expected_conditions.visibility_of_element_located(TestLocators.KONSTRUKTOR_PROVERKA))








