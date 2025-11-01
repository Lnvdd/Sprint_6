from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click_element(self, locator):
        element = self.find_clickable_element(locator)
        element.click()
    
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def send_keys_to_element(self, locator, keys):
        element = self.find_visible_element(locator)
        element.send_keys(keys)
    
    def get_element_text(self, locator):
        element = self.find_visible_element(locator)
        return element.text.strip()
    
    def scroll_page(self, x=0, y=300):
        self.driver.execute_script(f"window.scrollBy({x}, {y});")
    
    def click_body(self):
        self.driver.find_element(By.TAG_NAME, "body").click()
    
    def wait_for_url_change(self, expected_url):
        self.wait.until(lambda d: d.current_url == expected_url)
    
    def wait_for_multiple_windows(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
