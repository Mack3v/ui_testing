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

    def find_element(self, selector: str):
        return self.page.query_selector(selector)

    def click_element(self, selector: str) -> None:
        element = self.find_element(selector)
        if element:
            element.click()

    def input_text(self, selector: str, text: str) -> None:
        element = self.find_element(selector)
        if element:
            element.fill(text)

    def get_text(self, selector: str):
        element = self.find_element(selector)
        return element.text if element else None

    def is_element_visible(self, selector: str) -> bool:
        element = self.find_element(selector)
        return True if element and element.is_visible() else False

    def is_element_enabled(self, selector: str) -> bool:
        element = self.find_element(selector)
        return True if element and element.is_enabled() else False

    def is_element_present(self, selector: str) -> bool:
        return bool(self.find_element(selector))
