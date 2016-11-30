from interfaces import AbstractSubMenuItem


class SubMenuItem(AbstractSubMenuItem):
    def __init__(self):
        pass

    def get_submenu(self):
        pass

    def set_submenu(self):
        pass

    def delete_submenu(self):
        pass

    submenu = property(get_submenu, set_submenu, delete_submenu)