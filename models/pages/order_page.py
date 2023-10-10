from selene import Browser, have, be


class OrderPage:

    def __init__(self, driver: Browser):
        self.driver = driver

    # нажатие на кнопку оформления заказа
    def open(self):
        self.driver.element('.btn_checkout_custom').click()
        return self

    def fill_data(self, full_name: str, email: str, phone_number: str):
        self.driver.element('#bx-soa-region button.pull-right').click()
        self.driver.element('#bx-soa-delivery button.pull-right').click()
        self.driver.element('#soa-property-1').type(full_name)
        self.driver.element('#soa-property-2').type(email)
        self.driver.element('#soa-property-25').type(phone_number)
        self.driver.element('#bx-soa-properties button.pull-right').click()
        return self

    def save(self):
        self.driver.element('#bx-soa-total .btn-primary').click()
        return self

    def popup_window(self):
        self.driver.element('.main-user-consent-request-popup-header').wait_until(
            have.text('Согласие на обработку персональных данных'))
        return self

    def popup_not_accept(self):
        self.driver.element('.main-user-consent-request-popup-button-rej').should(
            be.clickable).click()
        return self
