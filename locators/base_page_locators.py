from selenium.webdriver.common.by import By


class BasePageLocators:
    GET_COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать']")
    LOGO_YANDEX = (By.XPATH, ".//img[@alt='Yandex']")
    LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']")

    BUTTON_HEADER_ORDER = (By.XPATH, "(//button[text()='Заказать'])[1]")
    BUTTON_MIDDLE_ORDER = (By.XPATH, "(//button[text()='Заказать'])[2]")
