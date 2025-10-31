import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
import time

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qa-scooter.praktikum-services.ru/"
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.url)
        time.sleep(1)
    
    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_TOP))
        button.click()
        time.sleep(1)
    
    @allure.step("Прокрутить до нижней кнопки 'Заказать'")
    def scroll_to_order_button_bottom(self):
        button = self.wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON_BOTTOM))
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(0.5)
    
    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM))
        button.click()
        time.sleep(1)
    
    @allure.step("Нажать на вопрос в FAQ")
    def click_faq_question(self, question_index):
        question_locator = (By.XPATH, MainPageLocators.FAQ_QUESTION_TEMPLATE.format(question_index))
        question = self.wait.until(EC.presence_of_element_located(question_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question)
        time.sleep(0.5)
        try:
            question.click()
        except:
            self.driver.execute_script("arguments[0].click();", question)
        time.sleep(0.5)
    
    @allure.step("Получить текст ответа")
    def get_faq_answer_text(self, question_index):
        answer_locator = (By.XPATH, MainPageLocators.FAQ_ANSWER_TEMPLATE.format(question_index))
        answer = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer.text.strip()
    
    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO))
        logo.click()
        time.sleep(1)
    
    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO))
        logo.click()
        time.sleep(1)