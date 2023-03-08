import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.questions_page_locators import QuestionsPageLocators
from pages.base_page import BasePage
from conftest import TIME_TO_WAIT_ELEMENTS


class QuestionsPage(BasePage):

    @allure.step('Найти вопрос и нажать на него по порядку')
    def find_question(self, question_locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*question_locator))
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(expected_conditions.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()

    @allure.step('Найти ответ и проверить формулировку')
    def find_answer(self, answer_locator):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(
            expected_conditions.visibility_of_element_located(QuestionsPageLocators.OPEN_ANSWER_TEXT))
        assert self.driver.find_element(*QuestionsPageLocators.OPEN_ANSWER_TEXT).text == answer_locator[1].split('\'')[1]
