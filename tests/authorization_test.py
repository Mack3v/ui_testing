import pytest

from pages.login_page import LoginPage


@pytest.mark.no_auth
@pytest.mark.login_page
class TestAuthorizationPage:

    def test_login_form_visibility(self, login_page: LoginPage):
        """
        Тест отображения формы логина на странице
        :param login_page: экземпляр страницы
        :return: None
        """
        login_page.placeholders_present()
        login_page.login_button.should_be_visible()
