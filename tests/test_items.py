import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestSearchPage:

    def test_add_item_to_cart(
        self,
        login_page: LoginPage,
        products_page: ProductsPage,
    ):
        products_page.check_products_count(6)
        products_page.add_item_to_card("backpack")
        products_page.check_remove_item_button("backpack")
        products_page.check_products_in_shopping_cart_count("1")
        products_page.open_shopping_cart()
        products_page.open_checkout_form()
