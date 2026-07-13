import allure
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import (
    ORDER_CONFIRM_BUTTON,
    ORDER_FIELD_ADDRESS,
    ORDER_FIELD_METRO,
    ORDER_FIELD_NAME,
    ORDER_FIELD_PHONE,
    ORDER_FIELD_SURNAME,
    ORDER_NEXT_BUTTON,
    ORDER_SUBMIT_BUTTON,
    ORDER_SUCCESS_TITLE,
    RENT_COLOR_BLACK,
    RENT_COLOR_GREY,
    RENT_COMMENT,
    RENT_DATE_INPUT,
    RENT_DATEPICKER,
    RENT_PERIOD_DROPDOWN,
    RENT_PERIOD_OPTIONS,
)
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнить форму «Для кого самокат»')
    def fill_customer_form(self, name, surname, address, metro, phone):
        self.type_text(ORDER_FIELD_NAME, name)
        self.type_text(ORDER_FIELD_SURNAME, surname)
        self.type_text(ORDER_FIELD_ADDRESS, address)
        self._select_metro(metro)
        self.type_text(ORDER_FIELD_PHONE, phone)
        self._click_next_button()

    @allure.step('Заполнить форму «Про аренду»')
    def fill_rent_form(self, date, period, color, comment):
        self._fill_date(date)
        self._select_rent_period(period)
        color_locator = RENT_COLOR_BLACK if color == 'black' else RENT_COLOR_GREY
        self.click(color_locator)
        self.type_text(RENT_COMMENT, comment)

    @allure.step('Подтвердить заказ')
    def submit_order(self):
        order_button = self.wait_for_clickable(ORDER_SUBMIT_BUTTON)
        self.scroll_to_element(order_button)
        self.js_click(order_button)

        confirm_button = self.wait_for_clickable(ORDER_CONFIRM_BUTTON)
        self.scroll_to_element(confirm_button)
        self.js_click(confirm_button)
        self.wait_for_visible(ORDER_SUCCESS_TITLE)

    @allure.step('Проверить успешность оформления заказа')
    def is_order_successful(self):
        title = self.wait_for_visible(ORDER_SUCCESS_TITLE)
        return 'Заказ оформлен' in title.text

    @allure.step('Выбрать станцию метро: {metro}')
    def _select_metro(self, metro):
        self.wait_for_visible(ORDER_FIELD_METRO)
        self.clear_locator(ORDER_FIELD_METRO)
        prefix = metro[:3]
        self.send_keys_to_locator(ORDER_FIELD_METRO, prefix)

        self.wait_for_attribute_starts_with(ORDER_FIELD_METRO, 'value', prefix)

        for _ in range(10):
            self.send_keys_to_locator(ORDER_FIELD_METRO, Keys.ARROW_DOWN)
            current_value = self.get_attribute(ORDER_FIELD_METRO, 'value')
            if current_value.strip().lower() == metro.strip().lower():
                self.send_keys_to_locator(ORDER_FIELD_METRO, Keys.ENTER)
                break
        else:
            self.send_keys_to_locator(ORDER_FIELD_METRO, Keys.ENTER)

        self.wait_for_attribute_equals(
            ORDER_FIELD_METRO, 'value', metro, normalize=True
        )
        self.wait_for_visible(ORDER_FIELD_PHONE)

    @allure.step('Перейти к следующему шагу формы')
    def _click_next_button(self):
        next_button = self.find_element(ORDER_NEXT_BUTTON)
        self.scroll_to_element(next_button)
        self.js_click(next_button)
        self.wait_for_visible(RENT_PERIOD_DROPDOWN)

    @allure.step('Указать дату аренды: {date}')
    def _fill_date(self, date):
        date_input = self.find_element(RENT_DATE_INPUT)
        self.scroll_to_element(date_input)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        self.wait_for_invisible(RENT_DATEPICKER)

    @allure.step('Выбрать срок аренды: {period}')
    def _select_rent_period(self, period):
        dropdown = self.wait_for_clickable(RENT_PERIOD_DROPDOWN)
        self.scroll_to_element(dropdown)
        dropdown.click()

        self.wait_for_visible(RENT_PERIOD_OPTIONS)
        for option in self.find_elements(RENT_PERIOD_OPTIONS):
            if option.text.strip().lower() == period.strip().lower():
                self.scroll_to_element(option)
                option.click()
                return

        raise ValueError(f'Не найден срок аренды: {period}')
