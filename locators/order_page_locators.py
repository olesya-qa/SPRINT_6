from selenium.webdriver.common.by import By

ORDER_FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
ORDER_FIELD_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
ORDER_FIELD_ADDRESS = (
    By.XPATH,
    "//input[@placeholder='* Адрес: куда привезти заказ']",
)
ORDER_FIELD_METRO = (By.CSS_SELECTOR, 'input.select-search__input')
ORDER_FIELD_PHONE = (
    By.XPATH,
    "//input[@placeholder='* Телефон: на него позвонит курьер']",
)
ORDER_NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

RENT_DATE_INPUT = (
    By.XPATH,
    "//input[contains(@placeholder,'Когда привезти')]",
)
RENT_PERIOD_DROPDOWN = (
    By.XPATH,
    "//div[contains(@class,'Dropdown-root')]",
)
RENT_PERIOD_OPTIONS = (By.CSS_SELECTOR, 'div.Dropdown-option')
RENT_COLOR_BLACK = (By.ID, 'black')
RENT_COLOR_GREY = (By.ID, 'grey')
RENT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

ORDER_SUBMIT_BUTTON = (
    By.XPATH,
    "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']",
)
ORDER_CONFIRM_BUTTON = (
    By.XPATH,
    "//div[contains(@class,'Order_Modal')]//button[text()='Да']",
)
ORDER_SUCCESS_TITLE = (
    By.XPATH,
    "//*[contains(text(),'Заказ оформлен')]",
)
