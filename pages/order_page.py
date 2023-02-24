import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Нажать кнопку для создания заказа')
    def click_order_button(self, by_button):
        self.click(by_button)

    @allure.step('Заполнить данные заказчика')
    def fill_customer_data(self, firstname, lastname, address, station, phone):
        self.send_data(OrderPageLocators.FIELD_FIRSTNAME, firstname)
        self.send_data(OrderPageLocators.FIELD_LASTNAME, lastname)
        self.send_data(OrderPageLocators.FIELD_ADDRESS, address)
        self.send_data(OrderPageLocators.FIELD_STATION, station)
        self.click(OrderPageLocators.SELECTED_STATION)
        self.send_data(OrderPageLocators.FIELD_PHONE, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_button_next(self):
        self.click(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполняем детали заказа')
    def fill_order_data(self, date, duration, color, comment):
        self.send_data(OrderPageLocators.FIELD_DATE, date)
        self.click(OrderPageLocators.DROPDOWN_ARROW)
        self.click(OrderPageLocators.FIELD_DROPDOWN_OPTION[duration])
        self.click(OrderPageLocators.FIELD_SCOOTER_COLORS[color])
        self.send_data(OrderPageLocators.FIELD_COMMENT, comment)

    @allure.step('Нажать кнопку для отправки заказа')
    def click_button_to_submit(self):
        self.click(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Нажать кнопку для подтверждения заказа')
    def click_button_confirm(self):
        self.click(OrderPageLocators.BUTTON_CONFIRM)

    @allure.step('Проверяем наличие модального окна с номером заказа')
    def verify_if_order_is_created(self):
        return self.find_text(OrderPageLocators.MODAL_WINDOW_WITH_ODER_NUMBER)
