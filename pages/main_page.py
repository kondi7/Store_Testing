from playwright.sync_api import Page, Locator
from settings.params import settings


class MainPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def login_button(self) -> Locator:
        return self.page.locator("[data-test=\"login-button\"]")

    @property
    def customer_login_field(self) -> Locator:
        return self.page.locator("[data-test=\"username\"]")

    @property
    def customer_password_field(self) -> Locator:
        return self.page.locator("[data-test=\"password\"]")

    def login_to_store(self, user_data) -> None:
        self.customer_login_field.fill(user_data["username"])
        self.customer_password_field.fill(user_data["password"])
        self.login_button.click()

    def navigate(self) -> None:
        self.page.goto(settings.TEST_URL)
