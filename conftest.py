import pytest
from playwright.sync_api import Browser, Page, sync_playwright

from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from components.side_bar import SideBar
from yaml_reader import read_config


@pytest.fixture(scope="session")
def config():
    return read_config()


@pytest.fixture(scope="session")
def chromium_page(config) -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        page = chromium.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto(config["BASE_URL"])
        yield page
        chromium.close()


@pytest.fixture(scope="session")
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(chromium_page)


@pytest.fixture(scope="session")
def products_page(chromium_page: Page) -> ProductsPage:
    return ProductsPage(chromium_page)


@pytest.fixture(scope="session")
def login(login_page, config):
    login_page.visit("https://www.saucedemo.com/")
    login_page.visit(config["BASE_URL"])
    login_page.authorization("standard_user", "secret_sauce")
    yield


@pytest.fixture(scope="function", autouse=False)
def logout(chromium_page):
    yield
    side_bar = SideBar(chromium_page)
    side_bar.logout()
