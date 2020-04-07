# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    old_groups = db.get_group_list()
    #index = randrange(len(old_groups))
    group_old = random.choice(old_groups)
    id = group_old.id
    group_new = Group(id = id, name="edit_Lenks", header="edit_Lenks", footer="edit_Lenknks")
    #group.id = old_groups[index].id
    #app.group.edit_group_by_index(index, group)
    app.group.edit_group_by_id(id, group_new)
    new_groups = db.get_group_list()
    # ищем в старом списке группу с рабочим id, которую надо обновить, и обновляем

    for i in range(len(old_groups)):
        if old_groups[i].id == id:
            old_groups[i] = group_new

    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


# def test_edit_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#
#     old_groups = app.group.get_group_list()
#     group = Group(name="New_name")
#     group.id = old_groups[0].id
#
#     app.group.edit_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
#
# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#
#     old_groups = app.group.get_group_list()
#     group = Group(header="New_header")
#     group.id = old_groups[0].id
#
#     app.group.edit_first_group(group)
#
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
#
# def test_edit_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     group = Group(footer="New_footer")
#     group.id = old_groups[0].id
#
#     app.group.edit_first_group(group)
#
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)