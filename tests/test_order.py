import allure
import pytest

from data import ORDER_DATA_SET_1, ORDER_DATA_SET_2
from pages.home_page import HomePage
from pages.order_page import OrderPage


@allure.feature('Заказ самоката')
class TestOrder:

    @allure.title('Позитивный сценарий заказа: {order_data[name]} {order_data[surname]}')
    @pytest.mark.parametrize(
        'order_data, entry_point',
        [
            (ORDER_DATA_SET_1, 'header'),
            (ORDER_DATA_SET_2, 'footer'),
        ],
        ids=['header_entry', 'footer_entry'],
    )
    def test_order_scooter_positive_flow(self, driver, order_data, entry_point):
        home_page = HomePage(driver)
        home_page.accept_cookies()

        if entry_point == 'header':
            home_page.click_order_button_header()
        else:
            home_page.click_order_button_footer()

        order_page = OrderPage(driver)
        order_page.fill_customer_form(
            name=order_data['name'],
            surname=order_data['surname'],
            address=order_data['address'],
            metro=order_data['metro'],
            phone=order_data['phone'],
        )
        order_page.fill_rent_form(
            date=order_data['date'],
            period=order_data['period'],
            color=order_data['color'],
            comment=order_data['comment'],
        )
        order_page.submit_order()

        assert order_page.is_order_successful()
