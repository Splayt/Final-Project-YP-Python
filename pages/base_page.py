import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from conftest import LINK_BASE_PAGE, TIME_TO_WAIT_ELEMENTS, LINK_DZEN


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(LINK_BASE_PAGE)

    @allure.step('Принять cookies')
    def accept_cookies(self):
        self.driver.find_element(*BasePageLocators.GET_COOKIE_BUTTON).click()

    def click(self, by_locator):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(expected_conditions.visibility_of_element_located(by_locator)).click()

    def send_data(self, by_locator, text):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def find_text(self, by_locator):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(
            expected_conditions.visibility_of_element_located(by_locator))
        return self.driver.find_element(*by_locator).text

    def navigate_to_link(self, by_locator, target):
        self.driver.find_element(*by_locator).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(expected_conditions.url_to_be(target))
        return self.driver.current_url

    @allure.step('Переход к логотипу Яндекса')
    def verify_if_link_to_yandex_works(self):
        self.driver.get(LINK_BASE_PAGE)
        return self.navigate_to_link(BasePageLocators.LOGO_YANDEX, LINK_DZEN)

    @allure.step('Переход к логотипу самоката')
    def verify_if_link_to_base_page_works(self):
        self.driver.get(LINK_BASE_PAGE)
        return self.navigate_to_link(BasePageLocators.LOGO_SCOOTER, LINK_BASE_PAGE)
