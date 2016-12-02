import pytest
from menu import header_menu


def test_001_create_add_child():
    top_menu = {
        'parent': 'root',
        'title': 'Fashon and Style',
        'order': 1,
        'link': 'http://www.google.com',
        'gender': 'men'
    }

    top = header_menu.HeaderMenu(top_menu)
    top_id = top.create()

    sub_menu = {
        'parent': top_id,
        'link': 'http://www.google.com',
        'title': 'Featured',
    }

    for _ in range(4):
        sub = header_menu.Submenu(sub_menu)
        sub_id = sub.create()
        top.add_child(sub_id)
        for _ in range(4):
            section = {
                'parent': sub_id,
                'type': 'product',
            }
            sec = header_menu.MenuSection(section)
            sec_id = sec.create()
            sub.add_child(sec_id)
            for i in range(4):
                product = {
                    'parent': sec_id,
                    'ref': 'ref_UUID' + str(i)
                }
                sec.add_child(product['ref'])

        # top.delete()

        #test_001_create_add_child()
        # data = [{
        #             'order': 1,
        #             'title': 'Fashion and Style',
        #             'link': 'http://google.com'
        #         } for _ in range(4)]
        #
        # sm = [{
        #           'title': "Hallo",
        #           'link': "yandex.com",
        #           'sections': None
        #       } for _ in range(4)]
        #
        # for item, submenu in zip(data, sm):
        #     sub_m = header_menu.Submenu(submenu)
        #     menu = header_menu.HeaderMenu(item)
        #
        #     sub_m.create()
        #
        #     menu.add_child(sub_m)
        #     menu.create()
        #
        # def test_001_