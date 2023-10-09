from selene import Browser
from models.pages.main_page import MainPage
from models.pages.search_page import SearchPage
from models.pages.basket_page import BasketPage
from models.pages.favorites_page import FavoritePage
from models.pages.order_page import OrderPage
from models.pages.auth_page import AuthPage


class ApplicationManager:

    def __init__(self, driver: Browser):
        self.site = MainPage(driver)
        self.search = SearchPage(driver)
        self.basket = BasketPage(driver)
        self.favorite = FavoritePage(driver)
        self.order = OrderPage(driver)
        self.auth = AuthPage(driver)
