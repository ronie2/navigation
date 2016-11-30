__all__ = ['AbstractMenu']


class AbstractMenu:
    def get_menu_items(self):
        raise NotImplementedError

    def add_menu_item(self):
        raise NotImplementedError

    def delete_menu_item(self):
        raise NotImplementedError
