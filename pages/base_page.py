from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Найти кликабельный элемент')
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Найти видимый элемент')
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Кликнуть на элемент')
    def click_element(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Прокрутить страницу')
    def scroll_page(self, x=0, y=300):
        self.driver.execute_script(f"window.scrollBy({x}, {y});")

    @allure.step('Отправить текст в элемент')
    def send_keys_to_element(self, locator, keys):
        element = self.find_visible_element(locator)
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_element_text(self, locator):
        element = self.find_visible_element(locator)
        return element.text.strip()

    @allure.step('Кликнуть на body')
    def click_body(self):
        self.driver.find_element(By.TAG_NAME, "body").click()

    @allure.step('Ожидать изменения URL')
    def wait_for_url_change(self, expected_url):
        self.wait.until(lambda d: d.current_url == expected_url)

    @allure.step('Ожидать появления нескольких окон')
    def wait_for_multiple_windows(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)

    @allure.step('Переключиться на окно')
    def switch_to_window(self, window_index):
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться перехода на dzen.ru')
    def wait_for_dzen_redirect(self, timeout=40):
        def dzen_loaded(drv):
            try:
                url = drv.current_url
                return url and "dzen.ru" in url
            except Exception:
                return False
        WebDriverWait(self.driver, timeout).until(dzen_loaded)