import allure
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.locators import OrderPageLocators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    @allure.step("Заполнить форму 'Для кого самокат'")
    def fill_personal_data(self, first_name, last_name, address, metro, phone):
        first_name_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.FIRST_NAME_INPUT))
        first_name_input.send_keys(first_name)
        last_name_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.LAST_NAME_INPUT))
        last_name_input.send_keys(last_name)
        address_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.ADDRESS_INPUT))
        address_input.send_keys(address)
        metro_input = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_STATION_INPUT))
        metro_input.click()
        time.sleep(0.5)
        metro_input.send_keys(metro)
        time.sleep(1)
        metro_input.send_keys(Keys.DOWN)
        time.sleep(0.3)
        metro_input.send_keys(Keys.ENTER)
        time.sleep(0.5)
        phone_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.PHONE_INPUT))
        phone_input.send_keys(phone)
        time.sleep(0.5)
    
    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        next_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        next_button.click()
        time.sleep(1.5)
    
    @allure.step("Заполнить форму 'Про аренду'")
    def fill_rental_data(self, delivery_date, rental_period, color, comment=""):
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(0.5)
        date_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DELIVERY_DATE_INPUT))
        date_input.click()
        time.sleep(0.3)
        date_input.send_keys(delivery_date)
        time.sleep(1)
        self.driver.find_element(By.TAG_NAME, "body").click()
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(0.5)
        dropdown = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))
        dropdown.click()
        time.sleep(1)
        period_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='Dropdown-option' and contains(text(), '{rental_period}')]")))
        period_option.click()
        time.sleep(0.5)
        if color == "black":
            checkbox = self.wait.until(EC.presence_of_element_located(OrderPageLocators.COLOR_BLACK_CHECKBOX))
            self.driver.execute_script("arguments[0].click();", checkbox)
        elif color == "grey":
            checkbox = self.wait.until(EC.presence_of_element_located(OrderPageLocators.COLOR_GREY_CHECKBOX))
            self.driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(0.5)
        if comment:
            comment_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.COMMENT_INPUT))
            comment_input.send_keys(comment)
        time.sleep(0.5)
    
    @allure.step("Нажать кнопку 'Заказать' и подтвердить")
    def submit_order(self):
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(0.5)
        order_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON_FINAL))
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)
        time.sleep(0.3)
        order_button.click()
        time.sleep(1.5)
        confirm_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON))
        confirm_button.click()
        time.sleep(1.5)
    
    @allure.step("Проверить отображение сообщения об успехе")
    def is_success_message_displayed(self):
        try:
            message = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE))
            return message.is_displayed()
        except:
            return False