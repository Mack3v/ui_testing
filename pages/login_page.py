from playwright.sync_api import Page

from page_factory.input import Input
from page_factory.button import Button
from page_factory.title import Title
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.login_input = Input(page, locator="#user-name", name="Login input")
        self.password_input = Input(page, locator="#password", name="Password input")
        self.login_button = Button(page, locator="#login-button", name="Login button")
        self.login_placeholder = Title(
            page, locator="[data-test='username']", name="Login title"
        )
        self.password_placeholder = Title(
            page, locator="[data-test='password']", name="Password placeholder"
        )
        self.error_msg = Title(
            page, locator="[data-test='error']", name="Error message"
        )

    def authorization(self, name: str, password: str):
        self.login_input.fill(value=name)
        self.password_input.fill(value=password)
        self.login_button.click()

    def placeholders_present(self):
        self.login_placeholder.should_be_visible()
        self.password_placeholder.should_be_visible()
        self.login_placeholder.should_have_attribute("placeholder", "Username")
        self.password_placeholder.should_have_attribute("placeholder", "Password")

    def check_error_message(self, text: str):
        self.error_msg.should_have_text(text)
