from selene import Browser, be, by


class FavoritePage:

    def __init__(self, driver: Browser):
        self.driver = driver

    # один клик - добавить в избранное, два - убрать из избранного на странице товара
    def add(self):
        self.driver.element('.border_svg').click()
        return self

    def open(self):
        self.driver.element('#favour_in').should(be.clickable).click()
        return self

    def check_items(self, item_name: str):
        self.driver.element(by.partial_text(item_name)).wait_until(be.visible)
        return self
