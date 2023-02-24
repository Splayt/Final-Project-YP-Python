from selenium.webdriver.common.by import By


class QuestionsPageLocators:
    QUESTION_1_COST = (By.ID, 'accordion__heading-0')
    QUESTION_2_COUNT = (By.ID, 'accordion__heading-1')
    QUESTION_3_TIME = (By.ID, 'accordion__heading-2')
    QUESTION_4_IS_TODAY = (By.ID, 'accordion__heading-3')
    QUESTION_5_CHANGE = (By.ID, 'accordion__heading-4')
    QUESTION_6_CHARGER = (By.ID, 'accordion__heading-5')
    QUESTION_7_CANCEL = (By.ID, 'accordion__heading-6')
    QUESTION_8_FARAWAY = (By.ID, 'accordion__heading-7')

    ANSWER_1_COST = (By.XPATH, "// p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    ANSWER_2_COUNT = (By.XPATH, "// p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")
    ANSWER_3_TIME = (By.XPATH, "// p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    ANSWER_4_IS_TODAY = (By.XPATH, "// p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    ANSWER_5_CHANGE = (By.XPATH, "// p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    ANSWER_6_CHARGER = (By.XPATH, "// p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")
    ANSWER_7_CANCEL = (By.XPATH, "// p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    ANSWER_8_FARAWAY = (By.XPATH, "// p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")

    OPEN_ANSWER_TEXT = (By.XPATH, ".//div[@role='region' and not(@hidden)]/p")
