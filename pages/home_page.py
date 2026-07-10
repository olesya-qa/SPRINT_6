import allure

from data import BASE_URL
from locators.base_page_locators import (
    COOKIE_BANNER,
    FAQ_ANSWERS,
    FAQ_BUTTONS,
    FAQ_SECTION,
    ORDER_BUTTON_FOOTER,
    ORDER_BUTTON_HEADER,
    ORDER_FIELD_NAME,
    SCOOTER_LOGO,
    YANDEX_LOGO,
)
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Открыть главную страницу')
    def open(self):
        self.open_url(BASE_URL)

    @allure.step('Принять cookies')
    def accept_cookies(self):
        self.click(COOKIE_BANNER)

    @allure.step('Нажать кнопку «Заказать» в шапке')
    def click_order_button_header(self):
        self.click(ORDER_BUTTON_HEADER)
        self.wait_for_visible(ORDER_FIELD_NAME)

    @allure.step('Нажать кнопку «Заказать» внизу страницы')
    def click_order_button_footer(self):
        button = self.wait_for_clickable(ORDER_BUTTON_FOOTER)
        self.scroll_to_element(button)
        self.js_click(button)
        self.wait_for_visible(ORDER_FIELD_NAME)

    @allure.step('Нажать на вопрос FAQ №{index}')
    def click_faq_question(self, index):
        self.scroll_to_locator(FAQ_SECTION)
        questions = self.find_elements(FAQ_BUTTONS)
        question = questions[index]
        self.scroll_to_element(question)
        self.js_click(question)

    @allure.step('Получить текст ответа FAQ №{index}')
    def get_faq_answer_text(self, index):
        answers = self.find_elements(FAQ_ANSWERS)
        answer = answers[index]
        self.wait_for_element_visible(answer)
        return answer.text.strip()

    @allure.step('Нажать на логотип Самоката')
    def click_scooter_logo(self):
        self.click(SCOOTER_LOGO)

    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.click(YANDEX_LOGO)
        self.wait_for_new_window_and_switch()
        self.wait_for_url_not_blank()
