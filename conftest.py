import pytest
from playwright.sync_api import Browser, Page, sync_playwright

from pages.products_page import ProductsPage
from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        yield chromium.new_page()


@pytest.fixture(scope='session')
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(chromium_page)


@pytest.fixture(scope='session')
def products_page(chromium_page: Page) -> ProductsPage:
    return ProductsPage(chromium_page)


@pytest.fixture(scope='session', autouse=True)
def login(login_page):
    login_page.visit('https://www.saucedemo.com/')
    login_page.placeholders_present(login_placeholder='Username', password_placeholder='Password')
    login_page.authorization('standard_user', 'secret_sauce')
    yield


@pytest.fixture(scope='session', autouse=True)
def logout(products_page):
    yield
    products_page.side_bar.logout()
