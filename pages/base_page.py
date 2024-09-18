from playwright.sync_api import Page, Response

from components.side_bar import SideBar


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.side_bar = SideBar(page)

    def visit(self, url: str) -> Response | None:
        return self.page.goto(url, wait_until='networkidle')

    def reload(self) -> Response | None:
        return self.page.reload(wait_until='domcontentloaded')

    def assert_url(self, expected_url: str) -> None:
        actual_url = self.page.url
        assert actual_url == expected_url, \
            f"URL не соответствует ожидаемому. Ожидался: '{expected_url}', Получен: '{actual_url}'"
