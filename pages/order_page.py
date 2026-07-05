import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
    RENT_PERIOD_DROPDOWN,
    RENT_PERIOD_OPTIONS,
)
from pages.base_page import BasePage


class OrderPage(BasePage):

    def fill_customer_form(self, name, surname, address, metro, phone):
        self.type_text(ORDER_FIELD_NAME, name)
        self.type_text(ORDER_FIELD_SURNAME, surname)
        self.type_text(ORDER_FIELD_ADDRESS, address)
        self._select_metro(metro)
        self.type_text(ORDER_FIELD_PHONE, phone)
        self._click_next_button()

    def fill_rent_form(self, date, period, color, comment):
        self._fill_date(date)
        self._select_rent_period(period)
        color_locator = RENT_COLOR_BLACK if color == 'black' else RENT_COLOR_GREY
        self.click(color_locator)
        self.type_text(RENT_COMMENT, comment)

    def submit_order(self):
        order_button = self.wait_for_clickable(ORDER_SUBMIT_BUTTON)
        self.scroll_to_element(order_button)
        self.js_click(order_button)

        confirm_button = self.wait_for_clickable(ORDER_CONFIRM_BUTTON)
        self.scroll_to_element(confirm_button)
        self.js_click(confirm_button)
        self.wait_for_visible(ORDER_SUCCESS_TITLE)

    def is_order_successful(self):
        title = self.wait_for_visible(ORDER_SUCCESS_TITLE)
        return 'Заказ оформлен' in title.text

    def _select_metro(self, metro):
        metro_input = self.wait_for_visible(ORDER_FIELD_METRO)
        metro_input.clear()
        prefix = metro[:3]
        metro_input.send_keys(prefix)
        time.sleep(1)

        WebDriverWait(self.driver, self.timeout).until(
            lambda driver: (
                driver.find_element(*ORDER_FIELD_METRO).get_attribute('value') or ''
            ).startswith(prefix)
        )

        for _ in range(10):
            metro_input = self.find_element(ORDER_FIELD_METRO)
            metro_input.send_keys(Keys.ARROW_DOWN)
            current_value = metro_input.get_attribute('value') or ''
            if current_value.strip().lower() == metro.strip().lower():
                metro_input.send_keys(Keys.ENTER)
                break
        else:
            metro_input = self.find_element(ORDER_FIELD_METRO)
            metro_input.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, self.timeout).until(
            lambda driver: (
                driver.find_element(*ORDER_FIELD_METRO).get_attribute('value') or ''
            ).strip().lower() == metro.strip().lower()
        )
        self.wait_for_visible(ORDER_FIELD_PHONE)

    def _click_next_button(self):
        next_button = self.find_element(ORDER_NEXT_BUTTON)
        self.scroll_to_element(next_button)
        self.js_click(next_button)
        self.wait_for_visible(RENT_PERIOD_DROPDOWN)

    def _fill_date(self, date):
        date_input = self.find_element(RENT_DATE_INPUT)
        self.scroll_to_element(date_input)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'react-datepicker'))
        )
        time.sleep(0.5)

    def _select_rent_period(self, period):
        dropdown = self.wait_for_clickable(RENT_PERIOD_DROPDOWN)
        self.scroll_to_element(dropdown)
        dropdown.click()

        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(RENT_PERIOD_OPTIONS)
        )
        for option in self.driver.find_elements(*RENT_PERIOD_OPTIONS):
            if option.text.strip().lower() == period.strip().lower():
                self.scroll_to_element(option)
                option.click()
                return

        raise ValueError(f'Не найден срок аренды: {period}')
