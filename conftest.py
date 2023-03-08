import pytest
from selenium import webdriver
from datetime import datetime, timedelta
from locators.questions_page_locators import QuestionsPageLocators
from locators.base_page_locators import BasePageLocators

LINK_BASE_PAGE = 'https://qa-scooter.praktikum-services.ru/'
LINK_DZEN = "https://dzen.ru/?yredirect=true"

TIME_TO_WAIT_ELEMENTS = 15
TEXT_ORDER_IS_DONE = "Заказ оформлен"

ORDERS = [{"by_button": BasePageLocators.BUTTON_MIDDLE_ORDER,
           "firstname": 'Игорь',
           "lastname": 'Алексеев',
           "address": 'Москва, ул. Ленина, 111 - 222',
           "phone": '+79265555555',
           "subway_station": 'Сокольники ',
           "date": (datetime.now() + timedelta(days=7)).strftime("%d.%m.%Y"),
           "duration": 7,
           "color": 'grey',
           "comment": 'Подъезд со стороны реки'
           },
          {"by_button": BasePageLocators.BUTTON_HEADER_ORDER,
           "firstname": 'Амелина',
           "lastname": 'Смирнова',
           "address": 'Москва, пер. Колотушкина, 10Б - 201',
           "phone": '+79100123456',
           "subway_station": 'Сокол ',
           "date": (datetime.now() + timedelta(days=3)).strftime("%d.%m.%Y"),
           "duration": 4,
           "color": 'black',
           "comment": 'Комментарий можно оставить на странице товара, сразу после нажатия кнопки «Заказать». Появится всплывающее окно, которое показано на картинке, где Вы сможете оставить комментарий к заказу, проверить информацию и добавить товар в корзину, либо отменить добавление.  '
           }
          ]

QUESTIONS_AND_ANSWERS = [[QuestionsPageLocators.QUESTION_1_COST, QuestionsPageLocators.ANSWER_1_COST],
                         [QuestionsPageLocators.QUESTION_2_COUNT, QuestionsPageLocators.ANSWER_2_COUNT],
                         [QuestionsPageLocators.QUESTION_3_TIME, QuestionsPageLocators.ANSWER_3_TIME],
                         [QuestionsPageLocators.QUESTION_4_IS_TODAY, QuestionsPageLocators.ANSWER_4_IS_TODAY],
                         [QuestionsPageLocators.QUESTION_5_CHANGE, QuestionsPageLocators.ANSWER_5_CHANGE],
                         [QuestionsPageLocators.QUESTION_6_CHARGER, QuestionsPageLocators.ANSWER_6_CHARGER],
                         [QuestionsPageLocators.QUESTION_7_CANCEL, QuestionsPageLocators.ANSWER_7_CANCEL],
                         [QuestionsPageLocators.QUESTION_8_FARAWAY, QuestionsPageLocators.ANSWER_8_FARAWAY]]


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(LINK_BASE_PAGE)

    yield driver

    driver.quit()
