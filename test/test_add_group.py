# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()

    group = Group(name="Lenks", header="Lenks", footer="Lenknks")
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



# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)