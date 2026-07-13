import allure

from data import ORDER_DATA_SET_1, ORDER_DATA_SET_2
from pages.home_page import HomePage
from pages.order_page import OrderPage


@allure.feature('Заказ самоката')
class TestOrder:

    @allure.title(
        'Позитивный сценарий заказа через шапку: '
        f'{ORDER_DATA_SET_1["name"]} {ORDER_DATA_SET_1["surname"]}'
    )
    def test_order_scooter_from_header(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_order_button_header()

        order_page = OrderPage(driver)
        order_page.fill_customer_form(
            name=ORDER_DATA_SET_1['name'],
            surname=ORDER_DATA_SET_1['surname'],
            address=ORDER_DATA_SET_1['address'],
            metro=ORDER_DATA_SET_1['metro'],
            phone=ORDER_DATA_SET_1['phone'],
        )
        order_page.fill_rent_form(
            date=ORDER_DATA_SET_1['date'],
            period=ORDER_DATA_SET_1['period'],
            color=ORDER_DATA_SET_1['color'],
            comment=ORDER_DATA_SET_1['comment'],
        )
        order_page.submit_order()

        assert order_page.is_order_successful()

    @allure.title(
        'Позитивный сценарий заказа через футер: '
        f'{ORDER_DATA_SET_2["name"]} {ORDER_DATA_SET_2["surname"]}'
    )
    def test_order_scooter_from_footer(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_order_button_footer()

        order_page = OrderPage(driver)
        order_page.fill_customer_form(
            name=ORDER_DATA_SET_2['name'],
            surname=ORDER_DATA_SET_2['surname'],
            address=ORDER_DATA_SET_2['address'],
            metro=ORDER_DATA_SET_2['metro'],
            phone=ORDER_DATA_SET_2['phone'],
        )
        order_page.fill_rent_form(
            date=ORDER_DATA_SET_2['date'],
            period=ORDER_DATA_SET_2['period'],
            color=ORDER_DATA_SET_2['color'],
            comment=ORDER_DATA_SET_2['comment'],
        )
        order_page.submit_order()

        assert order_page.is_order_successful()
