from interfaces import AbstractSubMenuSectionItem



class ArticleSMSectionItem(AbstractSubMenuSectionItem):
    def __init__(self, sm_section):
        self._sm_section = sm_section
        self._sm_section_items = self._collect_sm_section_items()

    def get_sm_section_item(self):
        return self._sm_section_items

    def add_sm_section_item(self, item):
        if not isinstance(item, AbstractSubMenuSectionItem):
            raise TypeError('Only "SubMenuItem" allowed')

        self._sm_section_items.append(item)

    def delete_sm_section_item(self, item):
        try:
            self._sm_section_items.remove(item)
        except ValueError:
            raise ValueError('No such section item in submenu')

    def _collect_sm_section_items(self):
        return [{'title': 'Hallo World',
                 'price': 2321,
                 'pic': 'http://google.com'}
                for _ in range(4)]


class ProductSMSectionItem(AbstractSubMenuSectionItem):
    def __init__(self):
        pass


class CategorySMSectionItem(AbstractSubMenuSectionItem):
    def __init__(self):
        pass
