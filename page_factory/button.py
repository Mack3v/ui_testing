from page_factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return 'button'

    def hover(self, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        locator.hover()

    def double_click(self, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.dblclick()

    def click(self, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.click()
