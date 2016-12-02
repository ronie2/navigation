from interfaces import AbstractSubMenuItem
from modeladapter import *


# "sections collections"
# {
# 	'_id': XXX,
# 	'section_type': 'products',
# 	'items':[product_id|article_id|category_id]
# }

def get_section_object(**kwargs):
    if 'products' in kwargs:
        return ProductSMSection

    elif 'articles' in kwargs:
        return ArticleSMSection

    elif 'category' in kwargs:
        return CategorySMSection

    else:
        raise RuntimeError('Type: {type} isn`t supported'.format(type=kwargs))


class ProductSMSection(AbstractSubMenuItem):
    def __init__(self, section_type):
        self._section_type = section_type
        self._items = []
        self._id = None
        self._table = 'menu_sections'
        self._init_connection(rethinkdb=True)

    def _init_connection(self, **kwargs):
        try:
            self._db_adapter = get_db_adapter(**kwargs)
            self._db_adapter.connect()
        except DBConnectionFailed:
            # TODO: Implement reconnect logic & some logging
            pass

    def _prepare_db_record(self):
        return {
            'section_type': self._section_type,
            'items': self._items
        }

    def add_item(self, item_id):
        self._items.append(item_id)

    def get_section_items(self):
        return self._items

    def insert_into_db(self):
        try:
            self._id = self._db_adapter.insert(
                self._table,
                self._prepare_db_record()
            )
        except DBCRUDFailed:
            # TODO: Implement save failed logic
            pass

    def get_section(self):
        try:
            result = self._db_adapter.get(self._table, self._id)
            return dict(result)
        except DBCRUDFailed:
            # TODO: Implement DB error logic
            pass
        except Exception:
            # TODO: Implement list, map, dict error logic
            pass

    def delete_section(self):
        try:
            self._db_adapter.delete(self._table, self._id)
        except DBCRUDFailed:
            # TODO: Implement delete dailed logic
            pass


class ArticleSMSection(AbstractSubMenuItem):
    def __init__(self):
        pass


class CategorySMSection(AbstractSubMenuItem):
    def __init__(self):
        pass
