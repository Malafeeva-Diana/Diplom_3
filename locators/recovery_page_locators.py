from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    # Кнопка Восстановить
    RECOVERY_BUTTON = [By.XPATH, './/button[text() = "Восстановить"]']
    # Кнопка Сохранить
    SAVE_BUTTON = [By.XPATH, './/button[text() = "Сохранить"]']
    # Кнопка переключения видимости пароля
    EYE_BUTTON = [By.XPATH, './/div[contains(@class, "icon-action")]']
    # Заголовок Восстановление пароля
    RECOVERY_HEADER = [By.XPATH, './/h2[text() = "Восстановление пароля"]']
    # Поле ввода Пароль
    FOCUSED_INPUT_PASSWORD = [By.XPATH, './/*[contains(@class,"input__placeholder")]']
