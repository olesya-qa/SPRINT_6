from selenium.webdriver.common.by import By

COOKIE_BANNER = (By.ID, 'rcc-confirm-button')

SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

ORDER_BUTTON_HEADER = (
    By.XPATH,
    "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']",
)
ORDER_BUTTON_FOOTER = (
    By.XPATH,
    "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']",
)

FAQ_SECTION = (By.CSS_SELECTOR, '.Home_FAQ__3uVm4')

FAQ_BUTTONS = (
    By.CSS_SELECTOR,
    "div.accordion__button[id^='accordion__heading-']",
)
FAQ_ANSWERS = (
    By.CSS_SELECTOR,
    "div.accordion__panel[id^='accordion__panel-']",
)

ORDER_FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
