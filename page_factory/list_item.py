from page_factory.component import Component
from typing import List


class ListItem(Component):
    @property
    def type_of(self) -> str:
        return 'list item'

    def find_all_items(self, **kwargs):
        return self.get_locator(**kwargs)
