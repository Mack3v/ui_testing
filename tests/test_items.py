import pytest

from pages.products_page import ProductsPage


@pytest.mark.inventory_page
class TestInventoryPage:
    """
    Тесты для страницы товаров
    """

    @pytest.mark.parametrize(
        "item, item_name",
        [
            ("backpack", "Sauce Labs Backpack"),
        ],
    )
    def test_add_item_to_cart(
        self, login, logout, products_page: ProductsPage, item, item_name
    ):
        """
        Тест заказа товара с общей страницы: добавление в корзину, заполнение формы заказа, финиш
        """
        products_page.add_item_to_card(item)
        products_page.check_remove_item_button(item)
        products_page.check_products_in_shopping_cart_count("1")
        products_page.open_shopping_cart()
        products_page.open_checkout_form()
        products_page.fill_checkout_form()
        products_page.open_confirm_order_page()
        products_page.check_item_name_in_order(item_name)
