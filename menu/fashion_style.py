from interfaces import AbstractMenuItem


class FashionAndStyle(AbstractMenuItem):
    def __init__(self):
        self._submenu_items = []

    def create_submenu_item(self, item):
        self._submenu_items.append(item)

    def delete_submenu_item(self, item):
        try:
            self._submenu_items.remove(item)
        except ValueError:
            raise ValueError('No such item in submenu. Nothing to delete')

    def update_submenu_item(self):
        pass

    def get_submenu_items(self):
        pass
