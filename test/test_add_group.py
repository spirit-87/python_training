# -*- coding: utf-8 -*-
from model.group import Group
from data.add_group import constant as testdata
import pytest


# Разделили тестовые данные и операции с ними
# Добавили генерацию случайных данных
# Добавили множ-во тестов со случ. данными

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    #pass
    old_groups = app.group.get_group_list()
    app.group.create(group)
    #для сравнения длин списков групп надо делать кучу обращений к браузера, а чтобы просто посчитать кол-во групп, надо
    #выполнить один запрос count() - хеш - используется для легкой проверки, если проверка прошла успешно, то можно пере-
    # ходить к более тяжеловесным проверкам
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    # для сортировки нужен ключ, если у группы нет id, то непонятно, как сортировать, но новая группа должна быть на последнем месте
    # и иметь самый большой id
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

# testdata = [Group(name=name, header=header, footer=footer)
#             for name in ["",random_string("name", 10)]
#             for header in ["", random_string("header", 10)]
#             for footer in ["", random_string("footer", 10)]
#             ]
