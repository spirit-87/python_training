# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "test"))
    app.contact.edit_first_contact(
        Contact("fn", "mn", "ln", "nn", "t", "c", "address", "5", "6", "7", "8", "e1", "e2", "e3",
                "www", "31", "May", "1234", "3", "July", "5678", "address", "6", "test"))


def test_edit_first_contact_name(app):
    app.contact.edit_first_contact(Contact("new_fn"))
