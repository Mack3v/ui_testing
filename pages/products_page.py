from playwright.sync_api import Page

from page_factory.list_item import ListItem
from page_factory.button import Button
from page_factory.title import Title
from page_factory.input import Input
from pages.base_page import BasePage
from data.checkout_data import CheckoutData


class ProductsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.product_card = ListItem(
            page, locator=".inventory_item", name="Product card"
        )
        self.login_button = Button(page, locator="#login-button", name="Login button")
        self.add_item_button = Button(
            page,
            locator="#add-to-cart-sauce-labs-{item_name}",
            name="Add product button",
        )
        self.remove_item_button = Button(
            page, locator="#remove-sauce-labs-{item_name}", name="Remove product button"
        )
        self.shopping_cart = Button(
            page, locator="#shopping_cart_container", name="Shopping cart"
        )
        self.checkout_button = Button(page, locator="#checkout", name="Checkout button")
        self.first_name_field = Input(
            page, locator="#first-name", name="First Name field"
        )
        self.last_name_field = Input(page, locator="#last-name", name="Last Name field")
        self.postal_code_field = Input(
            page, locator="#postal-code", name="Postal code field"
        )
        self.item_name = Title(
            page, locator=".inventory_item_name", name="Postal code field"
        )
        self.continue_button = Button(page, locator="#continue", name="Continue button")
        self.finish_button = Button(page, locator="#finish", name="Finish button")

    def check_products_count(self, count: int):
        product = self.product_card.find_all_items().all()
        assert (
            len(product) == count
        ), f"Ожидаемое количество: {count}\nПолученное: {len(product)}"

    def add_item_to_card(self, item_name: str):
        self.add_item_button.click(item_name=item_name)

    def check_remove_item_button(self, item_name: str):
        self.remove_item_button.should_be_visible(item_name=item_name)

    def check_products_in_shopping_cart_count(self, text: str):
        self.shopping_cart.should_have_text(text)

    def open_shopping_cart(self):
        self.shopping_cart.click()
        self.assert_url("https://www.saucedemo.com/cart.html")

    def open_checkout_form(self):
        self.checkout_button.click()
        self.assert_url("https://www.saucedemo.com/checkout-step-one.html")

    def fill_checkout_form(self):
        data = CheckoutData().generate_data()

        self.first_name_field.fill(data["first_name"])
        self.last_name_field.fill(data["last_name"])
        self.postal_code_field.fill(data["postal_code"])

    def check_item_name_in_order(self, text: str):
        self.item_name.should_have_text(text)

    def open_confirm_order_page(self):
        self.continue_button.click()
        self.assert_url("https://www.saucedemo.com/checkout-step-two.html")

    def finish_order(self):
        self.finish_button.click()
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
