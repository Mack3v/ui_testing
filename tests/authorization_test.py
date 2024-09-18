import pytest

from pages.login_page import LoginPage


@pytest.mark.no_auth
@pytest.mark.login_page
class TestAuthorizationPage:
    """
    Тесты для страницы авторизации
    """

    def test_login_form_visibility(self, login_page: LoginPage):
        """
        Тест отображения формы логина на странице
        """
        login_page.placeholders_present()
        login_page.login_button.should_be_visible()

    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("problem_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            ("error_user", "secret_sauce"),
            ("visual_user", "secret_sauce"),
        ],
    )
    def test_authorization(
        self, login_page: LoginPage, username, password, config, logout
    ):
        """
        Тест позитивной авторизации всех активных пользователей
        """
        login_page.authorization(name=username, password=password)
        login_page.assert_url(config["INVENTORY_URL"])

    def test_negative_authorization(self, login_page: LoginPage, config):
        """
        Тест негативной авторизации (заблокированный пользователь)
        """
        login_page.authorization(name="locked_out_user", password="secret_sauce")
        login_page.assert_url(config["BASE_URL"])
        login_page.check_error_message(
            "Epic sadface: Sorry, this user has been locked out."
        )
