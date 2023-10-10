from models.application_manager import ApplicationManager
import allure
import pytest


@pytest.fixture(scope='function')
def app(setup_browser) -> ApplicationManager:
    application = ApplicationManager(setup_browser)
    return application


@allure.description('Поиск несуществующего товара')
@allure.feature('Поиск')
def test_empty_search(app: ApplicationManager):
    with allure.step('Открываем стартовую страницу'):
        app.site.open()
    with allure.step('В строку поиска вводим значение и проверяем что товар не найден'):
        app.search.not_found('тестъ')


@allure.description('Поиск по автору')
@allure.feature('Поиск')
def test_author_search(app: ApplicationManager):
    with allure.step('Открываем стартовую страницу'):
        app.site.open()
    with allure.step('Переходим в раздел Авторы и ищем конкретного автора'):
        app.search.author(author_name='Лем С')


@allure.description('Добавление товаров в корзину')
@allure.feature('Корзина')
def test_add_items_to_basket(app: ApplicationManager):
    with allure.step('Открываем стартовую страницу'):
        app.site.open()
    with allure.step('Ищем товар и открываем его страницу'):
        app.search.input(value='Тест-дизайн').open_item_page()
    with allure.step('Добавляем товар в корзину'):
        app.basket.add_item()
    with allure.step('Ищем товар и открываем его страницу'):
        app.search.input(value='Виафоре').open_item_page()
    with allure.step('Добавляем товар в корзину и открываем ее'):
        app.basket.add_item().open()
    with allure.step('Проверяем количество товаров в корзине'):
        app.basket.check_quantity(2)
    with allure.step('Очищаем корзину'):
        app.basket.clear()


@allure.description('Добавление товаров в избранное')
@allure.feature('Избранное')
def test_add_items_to_favorite(app: ApplicationManager):
    with allure.step('Открываем стартовую страницу'):
        app.site.open()
    with allure.step('Ищем товар и открываем его страницу'):
        app.search.input(value='Тест-дизайн').open_item_page()
    with allure.step('Добавляем товар в избранное'):
        app.favorite.add()
    with allure.step('Ищем товар и открываем его страницу'):
        app.search.input(value='Виафоре').open_item_page()
    with allure.step('Добавляем товар в избранное и открываем список избранного'):
        app.favorite.add().open()
    with allure.step('Проверяем наличие в избранном ранее добавленных товаров'):
        app.favorite.check_items('Тест-дизайн').check_items('Харбанс')


@allure.description(
    'Отказ от обработки персональных данных на странице оформления заказа')
@allure.feature('Оформление заказа')
def test_order_registration(app: ApplicationManager):
    with allure.step('Открываем стартовую страницу'):
        app.site.open()
    with allure.step('Ищем товар и открываем страницу товара'):
        app.search.input(value='Тест-дизайн').open_item_page()
    with allure.step('Добавляем товар в корзину и открываем ее'):
        app.basket.add_item().open()
    with allure.step('Нажимаем в корзине Оформить заказ'):
        app.order.open()
    with allure.step('Заполняем данные'):
        app.order.fill_data(full_name='Тестовый Пользователь',
                            email='test@gmail.com',
                            phone_number='89118577463')
    with allure.step('Подтверждаем заполнение данных нажатием Оформление заказа'):
        app.order.save()
    with allure.step('Проверяем наличие всплывающего окна'):
        app.order.popup_window()
    with allure.step('Отказываемcя от обработки персональных данных'):
        app.order.popup_not_accept()


@allure.description('Ввод неверного промокода в корзине')
@allure.feature('Оформление заказа')
def test_invalid_coupon(app: ApplicationManager):
    with allure.step('Открываем стартовую страницу'):
        app.site.open()
    with allure.step('Ищем товар и открываем его страницу'):
        app.search.input(value='Тест-дизайн').open_item_page()
    with allure.step('Добавляем товар в корзину и открываем ее'):
        app.basket.add_item().open()
    with allure.step('Вводим невалидный промокод и проверяем что он не найден'):
        app.basket.enter_coupon('промокод').apply_coupon_button().check_invalid_coupon()


@allure.description('Неуспешная авторизация')
@allure.feature('Авторизация')
def test_failed_auth(app: ApplicationManager):
    with allure.step('Открываем стартовую страницу'):
        app.site.open()
    with allure.step(
            'Нажимаем на "Войти" и вводим данные незарегистрированного пользователя'):
        app.auth.open_auth_form().fill_login('test').fill_password(
            '12345678').submit_auth()
    with allure.step('Проверяем наличие алерта о неуспешной авторизации'):
        app.auth.auth_alert()
