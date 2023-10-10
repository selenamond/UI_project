from selene import Browser, have


class BasketPage:

    def __init__(self, driver: Browser):
        self.driver = driver

    def add_item(self):
        self.driver.element('.main-button-container').click()
        return self

    def open(self):
        self.driver.element('#bx_basketFKauiI').click()
        return self

    def check_quantity(self, quantity: int):
        self.driver.element('#basket-item-table').all('tr').should(have.size(quantity))
        return self

    def clear(self):
        self.driver.element('a[href="/basket/?clear"]').click()
        return self

    def enter_coupon(self, text):
        self.driver.element('.form-group .form-control').click()
        self.driver.element('.form-group .form-control').type(text)
        return self

    def apply_coupon_button(self):
        self.driver.element('.basket-coupon-block-coupon-btn').click()
        return self

    def check_invalid_coupon(self):
        self.driver.element('.basket-coupon-text').should(have.text('не найден'))
        return self
