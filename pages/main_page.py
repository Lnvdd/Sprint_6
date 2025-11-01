import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://qa-scooter.praktikum-services.ru/"
    
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.url)
    
    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
    
    @allure.step("Прокрутить до нижней кнопки 'Заказать'")
    def scroll_to_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    @allure.step("Нажать на вопрос в FAQ")
    def click_faq_question(self, question_index):
        question_locator = (By.XPATH, MainPageLocators.FAQ_QUESTION_TEMPLATE.format(question_index))
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
    
    @allure.step("Получить текст ответа")
    def get_faq_answer_text(self, question_index):
        answer_locator = (By.XPATH, MainPageLocators.FAQ_ANSWER_TEMPLATE.format(question_index))
        return self.get_element_text(answer_locator)
    
    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)