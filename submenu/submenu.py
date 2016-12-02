# "submenu_item"
# {
# 	'_id': XXX,
# 	'title': 'Featured',
#  	'link': 'http://google.com',
#  	'sections': [id, id, id]
# }

from interfaces import AbstractSubMenuItem
from modeladapter import *


class SubMenuItem(AbstractSubMenuItem):
    def __init__(self, title, link):
        self._title = title
        self._link = link
        self._sections = []
        self._init_connection(rethinkdb=True)
        self._table = 'submenu'

    def _init_connection(self, **kwargs):
        try:
            self._db_adapter = get_db_adapter(**kwargs)
            self._db_adapter.connect()
        except DBConnectionFailed:
            # TODO: Implement reconnect logic & some logging
            pass

    def _prepare_db_record(self):
        return {
            'title': self._title,
            'link': self._link,
            'sections': self._sections
        }

    def add_section(self, section_id):
        self._sections.append(section_id)

    def get_submenu(self):
        try:
            result = self._db_adapter.get(self._table, self._id)
            return dict(result)
        except DBCRUDFailed:
            # TODO: Implement DB error logic
            pass
        except Exception:
            # TODO: Implement dict error logic
            pass

    def insert_into_db(self):
        try:
            self._id = self._db_adapter.insert(
                self._table,
                self._prepare_db_record()
            )
        except DBCRUDFailed:
            # TODO: Implement save failed logic
            pass

    def delete_submenu(self):
        try:
            self._db_adapter.delete(self._table, self._id)
        except DBCRUDFailed:
            # TODO: Implement delete dailed logic
            pass
