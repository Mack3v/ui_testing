from playwright.sync_api import expect

from page_factory.component import Component


class Input(Component):
    @property
    def type_of(self) -> str:
        return 'input'

    def fill(self, value: str, validate_value=False, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.fill(value)

        if validate_value:
            self.should_have_value(value, **kwargs)

    def should_have_value(self, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
