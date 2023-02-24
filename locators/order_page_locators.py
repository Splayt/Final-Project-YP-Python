from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIELD_FIRSTNAME = (By.XPATH, "//input[@placeholder='* Имя']")
    FIELD_LASTNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    FIELD_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    FIELD_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    FIELD_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    SELECTED_STATION = (By.CSS_SELECTOR, '[class="select-search__select"]')
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    BUTTON_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    BUTTON_CONFIRM = (By.XPATH, "//button[text()='Да']")

    FIELD_DATE = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]
    DROPDOWN_ARROW = [By.XPATH, ".//*[@class='Dropdown-arrow']"]
    FIELD_DROPDOWN_OPTION = {
        1: [By.XPATH, "(//div[@class='Dropdown-option'])[1]"],
        2: [By.XPATH, "(//div[@class='Dropdown-option'])[2]"],
        3: [By.XPATH, "(//div[@class='Dropdown-option'])[3]"],
        4: [By.XPATH, "(//div[@class='Dropdown-option'])[4]"],
        5: [By.XPATH, "(//div[@class='Dropdown-option'])[5]"],
        6: [By.XPATH, "(//div[@class='Dropdown-option'])[6]"],
        7: [By.XPATH, "(//div[@class='Dropdown-option'])[7]"]
    }
    FIELD_SCOOTER_COLORS = {
        "black": [By.ID, 'black'],
        "grey": [By.ID, 'grey']
            }
    FIELD_COMMENT = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")
    MODAL_WINDOW_WITH_ODER_NUMBER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
