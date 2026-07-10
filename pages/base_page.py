from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_invisible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_element_visible(self, element):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of(element)
        )

    def wait_until(self, condition):
        return WebDriverWait(self.driver, self.timeout).until(condition)

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        self.scroll_to_element(element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.js_click(element)

    def type_text(self, locator, text):
        element = self.find_element(locator)
        self.scroll_to_element(element)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, element):
        self.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    def scroll_to_locator(self, locator):
        element = self.find_element(locator)
        self.scroll_to_element(element)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def js_click(self, element):
        self.execute_script('arguments[0].click();', element)

    def wait_for_new_window_and_switch(self):
        self.wait_until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_url_not_blank(self):
        self.wait_until(lambda driver: driver.current_url != 'about:blank')
