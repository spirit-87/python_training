# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="edit_Lenks", header="edit_Lenks", footer="edit_Lenknks"))


def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="New_name"))


def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="New_header"))


def test_edit_group_footer(app):
    app.group.edit_first_group(Group(footer="New_footer"))
