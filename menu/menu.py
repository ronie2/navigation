from interfaces import AbstractMenu, AbstractSubMenuItem


class Menu(AbstractMenu):
    def __init__(self):
        self._menu_items = []

    def get_menu_items(self):
        return self._menu_items

    def add_menu_item(self, item):
        if isinstance(item, AbstractSubMenuItem):
            self._menu_items.append(item)
        else:
            raise TypeError('Only "SubMenuItem" allowed')
