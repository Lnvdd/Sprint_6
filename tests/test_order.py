import pytest
import allure
import time
from pages.main_page import MainPage
from pages.order_page import OrderPage

ORDER_TEST_DATA = [
    {
        "first_name": "Иван",
        "last_name": "Петров",
        "address": "ул. Ленина, д. 10",
        "metro": "Сокольники",
        "phone": "+79991234567",
        "delivery_date": "31.10.2025",
        "rental_period": "сутки",
        "color": "black",
        "comment": "Позвоните за час"
    },
    {
        "first_name": "Мария",
        "last_name": "Сидорова",
        "address": "пр. Мира, д. 25",
        "metro": "Черкизовская",
        "phone": "+79997654321",
        "delivery_date": "02.11.2025",
        "rental_period": "двое суток",
        "color": "grey",
        "comment": ""
    }
]

@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий заказа")
class TestOrder:
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("test_data", ORDER_TEST_DATA)
    def test_order_top_button(self, driver, test_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open()
        main_page.click_order_button_top()
        order_page.fill_personal_data(test_data["first_name"], test_data["last_name"], test_data["address"], test_data["metro"], test_data["phone"])
        order_page.click_next_button()
        order_page.fill_rental_data(test_data["delivery_date"], test_data["rental_period"], test_data["color"], test_data["comment"])
        order_page.submit_order()
        assert order_page.is_success_message_displayed()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("test_data", ORDER_TEST_DATA)
    def test_order_bottom_button(self, driver, test_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open()
        main_page.scroll_to_order_button_bottom()
        main_page.click_order_button_bottom()
        order_page.fill_personal_data(test_data["first_name"], test_data["last_name"], test_data["address"], test_data["metro"], test_data["phone"])
        order_page.click_next_button()
        order_page.fill_rental_data(test_data["delivery_date"], test_data["rental_period"], test_data["color"], test_data["comment"])
        order_page.submit_order()
        assert order_page.is_success_message_displayed()

@allure.feature("Навигация")
@allure.story("Проверка логотипов")
class TestNavigation:
    @allure.severity(allure.severity_level.MINOR)
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button_top()
        main_page.click_scooter_logo()
        time.sleep(2)
        assert driver.current_url == main_page.url

    @allure.severity(allure.severity_level.MINOR)
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        original_window = driver.current_window_handle
        main_page.click_yandex_logo()
        time.sleep(5)
        windows = [w for w in driver.window_handles if w != original_window]
        if windows:
            driver.switch_to.window(windows[0])
            time.sleep(3)
        assert len(driver.window_handles) > 1