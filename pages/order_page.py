import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.locators import OrderPageLocators

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнить форму 'Для кого самокат'")
    def fill_personal_data(self, first_name, last_name, address, metro, phone):
        self.send_keys_to_element(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys_to_element(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        metro_input = self.find_clickable_element(OrderPageLocators.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro)
        metro_input.send_keys(Keys.DOWN)
        metro_input.send_keys(Keys.ENTER)
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму 'Про аренду'")
    def fill_rental_data(self, delivery_date, rental_period, color, comment=""):
        self.scroll_page(0, 300)
        date_input = self.find_visible_element(OrderPageLocators.DELIVERY_DATE_INPUT)
        date_input.click()
        date_input.send_keys(delivery_date)
        self.click_body()
        self.scroll_page(0, 300)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        period_option = self.find_clickable_element((By.XPATH, f"//div[@class='Dropdown-option' and contains(text(), '{rental_period}')]"))
        period_option.click()
        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK_CHECKBOX)
        elif color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY_CHECKBOX)
        if comment:
            self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Нажать кнопку 'Заказать' и подтвердить")
    def submit_order(self):
        self.scroll_page(0, 300)
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_FINAL)
        self.click_element(OrderPageLocators.ORDER_BUTTON_FINAL)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить отображение сообщения об успехе")
    def is_success_message_displayed(self):
        try:
            message = self.find_visible_element(OrderPageLocators.SUCCESS_MESSAGE)
            return message.is_displayed()
        except:
            return False