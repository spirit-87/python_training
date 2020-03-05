# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact("fn", "mn", "ln", "nn", "t", "c", "address", "5", "6", "7", "8", "e1", "e2", "e3",
                               "www", "31", "May", "1234", "3", "July", "5678", "address", "6", "test"))
