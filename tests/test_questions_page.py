import pytest
import allure
from pages.questions_page import QuestionsPage
from conftest import QUESTIONS_AND_ANSWERS


@allure.suite('Набор тестов для проверки вопросов и ответов')
class TestQuestionPage:

    @allure.title('Открыть dropdown-меню вопроса и проверить совпадение формулировки ответа ожидаемой.')
    @pytest.mark.parametrize('question, answer', QUESTIONS_AND_ANSWERS)
    def test_answer_matches_question_true(self, driver, question, answer):
        page = QuestionsPage(driver)
        page.accept_cookies()
        page.find_question(question)
        page.find_answer(answer)
