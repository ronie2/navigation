from interfaces import AbstractMenu, AbstractSubMenuItem
from submenu import submenu


class Menu(AbstractMenu):
    def __init__(self):
        self._menu_items = self._build_menu()

    def get_menu_items(self):
        return self._menu_items

    def add_menu_item(self, item):
        if isinstance(item, AbstractSubMenuItem):
            self._menu_items.append(item)
        else:
            raise TypeError('Only "SubMenuItem" allowed')

    def delete_menu_item(self, item):
        try:
            self._menu_items.remove(item)
        except ValueError:
            raise ValueError('No such item in menu. Nothing to delete')

    def _build_menu(self):
        return
