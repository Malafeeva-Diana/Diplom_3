import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_page import OrderPage
from conftest import driver
from data import Data


class TestOrderPage:
    @allure.title('Клик на заказ открывает окно с деталями')
    def test_order_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_feed_order()
        main_page.click_order_list_button()
        order_page = OrderPage(driver)
        order_page.click_order()
        assert order_page.order_modal_is_displayed() == True

    @allure.title('Заказы пользователя отображаются в Ленте заказов')
    def test_order_from_history_displayed_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_and_click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Data.data)
        main_page.ingredient_drag_and_drop()
        main_page.click_order_button()
        main_page.id_modal_is_displayed()
        order_number = main_page.get_order_number()
        main_page.click_modal_close()
        main_page.click_order_list_button()
        order_page = OrderPage(driver)
        assert order_number in order_page.get_last_order_number()

    @allure.title('При создании нового заказа счетчик Выполнено за все время/сегодня увеличивается')
    def test_count_orders(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)
        main_page.wait_click_account_butt()
        login_page.login_account(Data.data)
        main_page.click_order_list_butt()
        all_orders = order_page.get_count_all_orders()
        today_orders = order_page.get_count_today_orders()
        main_page.click_constructor_button()
        main_page.ingredient_drag_and_drop()
        main_page.click_order_button()
        main_page.click_modal_close()
        main_page.click_order_list_butt()
        update_all_orders = order_page.get_count_all_orders()
        update_today_orders = order_page.get_count_today_orders()
        assert update_all_orders > all_orders
        assert update_today_orders > today_orders

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_and_click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Data.data)
        main_page.ingredient_drag_and_drop()
        main_page.click_order_button()
        main_page.id_modal_is_displayed()
        order_number = main_page.get_order_number()
        main_page.click_modal_close()
        main_page.click_order_list_button()
        order_page = OrderPage(driver)
        assert order_number in order_page.get_order_in_work()
