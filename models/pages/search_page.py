from selene import Browser, by, be


class SearchPage:

    def __init__(self, driver: Browser):
        self.driver = driver

    def input(self, value: str):
        self.driver.element('#title-search-input').type(value).press_enter()
        self.driver.element(by.partial_text(value)).should(be.visible)
        return self

    def open_item_page(self):
        self.driver.element('.product_item_title').click()
        return self

    def not_found(self, value: str):
        self.driver.element('#title-search-input').type(value).press_enter()
        self.driver.element(by.partial_text(
            'К сожалению, на ваш поисковый запрос ничего не найдено.')).should(
            be.visible)
        return self

    def author(self, author_name: str):
        first_letter = author_name[0]
        self.driver.element('#header-top-line a[href*="/authors/"]').click()
        self.driver.element(f'.alphabet_list a[href*="{first_letter}"]').click()
        while True:
            if self.driver.element(by.partial_text(author_name)).matching(be.visible):
                self.driver.element(by.partial_text(author_name)).click()
            if not self.driver.element(by.partial_text(author_name)).matching(be.visible):
                break
            else:
                self.driver.all('.nav-next-title').first.click()
        return self
