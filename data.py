class Url:
    STELLAR_BURGERS = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_PAGE = f'{STELLAR_BURGERS}login'
    RECOVERY_PAGE = f'{STELLAR_BURGERS}forgot-password'
    RESET_PAGE = f'{STELLAR_BURGERS}reset-password'
    ORDER_LIST_PAGE = f'{STELLAR_BURGERS}feed'
    HISTORY_ORDER_PAGE = f'{STELLAR_BURGERS}account/order-history'


class Data:
    data = {
        'name': 'Диана',
        'email': 'malafeeva_diana_06089@ya.ru',
        'password': 'malafeeva_06'
    }


class TextAnswer:
    ingredient_modal_close = 'Соберите бургер'
    ingredient_modal_open = 'Детали ингредиента'
    ingredient_count = '2'
