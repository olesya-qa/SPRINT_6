import allure
import pytest

from data import FAQ_DATA
from pages.home_page import HomePage


@allure.feature('FAQ')
class TestFAQ:

    @allure.title('Вопрос: {faq_item[question]}')
    @pytest.mark.parametrize('index, faq_item', enumerate(FAQ_DATA))
    def test_faq_answer_opens(self, driver, index, faq_item):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_faq_question(index)

        answer_text = home_page.get_faq_answer_text(index)

        assert answer_text == faq_item['answer']
