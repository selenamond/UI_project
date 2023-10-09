from selene import Browser, have


class AuthPage:

    def __init__(self, driver: Browser):
        self.driver = driver

    def open_auth_form(self):
        self.driver.element(
            '//span[contains(text(),"Войти") and contains(@class,"icon-txt")]').click()
        return self

    def fill_login(self, login: str):
        self.driver.element('[name=USER_LOGIN]').click().type(login)
        return self

    def fill_password(self, password: str):
        self.driver.element('[name=USER_PASSWORD]').click().type(password)
        return self

    def submit_auth(self):
        self.driver.element('.form__widget-box [type=submit]').press_enter()
        return self

    def auth_alert(self):
        self.driver.element('.alert').should(have.text('Неверный логин или пароль.'))
        return self
