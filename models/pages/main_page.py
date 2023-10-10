from selene import Browser


class MainPage:

    def __init__(self, driver: Browser):
        self.driver = driver

    def open(self):
        self.driver.open('https://www.dom-knigi.ru/')
        return self
