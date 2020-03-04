# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact("fn", "mn", "ln", "nn", "t", "c", "address", "5", "6", "7", "8", "e1", "e2", "e3",
                               "www", "31", "May", "1234", "3", "July", "5678", "address", "6", "test"))
    app.session.logout()