from selenium.webdriver.common.by import By


class OrderListPageLocators:
    # Заказ
    ORDER = By.XPATH, './/li[contains(@class, "OrderHistory_listItem")]'
    # Последний заказ
    LAST_ORDER = By.XPATH, '//li[1]//p[@class="text text_type_digits-default"]'
    # Окно с деталями заказа
    ORDER_MODAL = By.XPATH, './/div[contains(@class, "Modal_orderBox")]'
    # Заказ в работе
    ORDER_IN_WORK = By.XPATH, './/*[contains(@class, "orderListReady")]//li[contains(@class,"digits-default")]'

    # Счетчик всех заказов
    ALL_ORDERS_COUNT = (
        By.XPATH, './/p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "digits-large")]')

    # Счетчик заказов за сегодня
    TODAY_ORDERS_COUNT = By.XPATH, ('.//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, '
                                    '"digits-large")]')
    # Последний заказ
    ORDER_LAST = (By.XPATH, '//ul[contains(@class, ''"OrderFeed_orderListReady")]/li[contains(@class, '
                            '"text_type_digits-default")]')
    BLOCK_ORDERS = (By.XPATH, '//ul[@class="OrderFeed_orderList__cBvyi"]/li')
    levyi_block_orders_lenta = (By.XPATH, './/p[@class="text text_type_digits-default"]')
