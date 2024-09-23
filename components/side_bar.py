from playwright.sync_api import Page

from page_factory.button import Button


class SideBar:
    """
    Боковое меню-бургер, отображаемое не всех страницах
    """

    def __init__(self, page: Page) -> None:
        self.page = page
        self.menu_button = Button(page, locator="#react-burger-menu-btn", name="Header")

        self.logout_button = Button(
            page, locator="#logout_sidebar_link", name="logout_button"
        )

    def open_menu(self):
        self.menu_button.click()

    def logout(self):
        self.open_menu()
        self.logout_button.click()
