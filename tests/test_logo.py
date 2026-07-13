import allure

from data import BASE_URL, DZEN_URL_PART
from pages.home_page import HomePage


@allure.feature('Логотипы')
class TestLogo:

    @allure.title('Логотип Самоката ведёт на главную страницу')
    def test_scooter_logo_opens_main_page(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_order_button_header()
        home_page.click_scooter_logo()

        assert home_page.get_current_url() == BASE_URL

    @allure.title('Логотип Яндекса открывает главную страницу Дзена')
    def test_yandex_logo_opens_dzen(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_yandex_logo()

        current_url = home_page.get_current_url()

        assert DZEN_URL_PART in current_url
