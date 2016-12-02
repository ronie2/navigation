from modeladapter import *


class VirtualMenu:
    def __init__(self, data):
        self._table = 'menu'

        self._children = []
        self._data = data

        try:
            self._parent = self._data['parent']
        except KeyError:
            # Every item should have 'parent'
            raise RuntimeError('Menu item SHOULD has `parent`')

        try:
            self._id = self._data['id']
            self._is_new = False
        except KeyError:
            # No 'id' -> this is new record
            self._id = None
            self._is_new = True

        self._init_connection(rethinkdb=True)
        self._create_table()

    def create(self):
        if not self._is_new:
            raise RuntimeError('Only new records may be created')
        try:
            self._id = self._db_adapter.insert(
                self._table,
                self._prepare_db_record()
            )
            self._is_new = False
            return self._id
        except DBCRUDFailed:
            # TODO: Implement save failed logic
            pass

    def read(self):
        if self._is_new:
            raise RuntimeError('Only existing records may be read')
        try:
            result = self._db_adapter.get(self._table, self._id)
            return dict(result)
        except DBCRUDFailed:
            # TODO: Implement DB error logic
            pass

    def update(self):
        if self._is_new:
            raise RuntimeError('Only existing records may be updated')
        try:
            self._db_adapter.update(
                self._table,
                self._prepare_db_record()
            )
        except DBCRUDFailed:
            # TODO: Implement update fail logic
            pass

    def delete(self):
        if self._is_new:
            raise RuntimeError('Only existing records may be deleted')
        try:
            self._delete_children(self._id)
            self._db_adapter.delete(self._table, self._id)
        except DBCRUDFailed:
            # TODO: Implement delete dailed logic
            pass

    def add_child(self, child_id):
        if child_id in self._children:
            raise RuntimeError('Submenu is already a child')
        self._children.append(child_id)
        self.update()

    def delete_child(self, child_id):
        if child_id not in self._children:
            raise RuntimeError('Submenu is not a child')
        self._delete_children(child_id)

    def _delete_children(self, node_id):
        try:
            record = self._db_adapter.get(self._table, node_id)
            if not record:
                # Child was not found in DB -> base case
                return
            children_ids = record['children']
            for child_id in children_ids:
                self._delete_children(child_id)
                self._db_adapter.delete(self._table, child_id)
        except KeyError:
            # Record has no 'children' -> base case
            return
        except DBCRUDFailed:
            # TODO: Implement DB read fail logic
            pass

    def _prepare_db_record(self):
        raise NotImplementedError

    def _init_connection(self, **kwargs):
        try:
            self._db_adapter = get_db_adapter(**kwargs)
            self._db_adapter.connect()
        except DBConnectionFailed:
            # TODO: Implement reconnect logic & some logging
            pass

    def _create_table(self):
        self._db_adapter.create_table(self._table)


class HeaderMenu(VirtualMenu):
    def __init__(self, data):
        super().__init__(data)

        self._title = self._data['title']
        self._order = self._data['order']
        self._link = self._data['link']
        self._gender = self._data['gender']

    def _prepare_db_record(self):
        record = {
            'order': self._order,
            'title': self._title,
            'link': self._link,
            'gender': self._gender,
            'children': self._children,
            'parent': 'root'
        }

        if not self._is_new:
            record['id'] = self._id

        return record


class Submenu(VirtualMenu):
    def __init__(self, data):
        super().__init__(data)

        self._title = self._data['title']
        self._link = self._data['link']

    def _prepare_db_record(self):
        record = {
            'title': self._title,
            'link': self._link,
            'parent': self._parent,
            'children': self._children
        }

        if not self._is_new:
            record['id'] = self._id

        return record


class MenuSection(VirtualMenu):
    def __init__(self, data):
        super().__init__(data)

        self._type = self._data['type']

    def _prepare_db_record(self):
        record = {
            'type': self._type,
            'parent': self._parent,
            'children': self._children
        }

        if not self._is_new:
            record['id'] = self._id

        return record
