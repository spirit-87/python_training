# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edit_Lenks", header="edit_Lenks", footer="edit_Lenknks"))
    app.session.logout()