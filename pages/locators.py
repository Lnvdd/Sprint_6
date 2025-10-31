from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    FAQ_QUESTION_TEMPLATE = "//div[@id='accordion__heading-{}']"
    FAQ_ANSWER_TEMPLATE = "//div[@id='accordion__panel-{}']"

class OrderPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    
    DELIVERY_DATE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-root')]//div[@class='Dropdown-placeholder']")
    RENTAL_PERIOD_OPTION_TEMPLATE = "//div[@class='Dropdown-option' and text()='{}']"
    
    COLOR_BLACK_CHECKBOX = (By.CSS_SELECTOR, "input#black")
    COLOR_GREY_CHECKBOX = (By.CSS_SELECTOR, "input#grey")
    
    COMMENT_INPUT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    ORDER_BUTTON_FINAL = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[contains(text(), 'Заказать')]")
    
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Заказ оформлен')]")

class MetroStationLocators:
    METRO_OPTION_TEMPLATE = "//div[contains(@class, 'select-search__option') and text()='{}']"
    METRO_LIST = (By.XPATH, "//div[contains(@class, 'select-search__option')]")
