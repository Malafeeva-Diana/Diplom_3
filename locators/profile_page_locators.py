from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Кнопка История заказов
    HISTORY_BUTTON = [By.XPATH, './/a[text() = "История заказов"]']
    # Кнопка Выход
    LOGOUT_BUTTON = [By.XPATH, './/button[text() = "Выход"]']
    # История заказов пользователя
    ORDER_HISTORY = [By.XPATH, './/div[contains(@class, "OrderHistory_textBox__3lgbs")]/p[contains(@class, '
                               '"text text_type_digits-default")])[last()]']
