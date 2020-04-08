# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_first_contact(app, db):
    if len(db.get_contact_list())== 0:
        app.contact.create(Contact(firstname = "test"))

    old_contacts = db.get_contact_list()
    contact_old = random.choice(old_contacts)
    id = contact_old.id
    contact_new = Contact("fn", "mn", "ln", "nn", "t", "c", "address", "5", "6", "7", "8", "e1", "e2", "e3",
                "www", "31", "May", "1234", "3", "July", "5678", "address", "6", "test")
    contact_new.id = id
    app.contact.edit_contact_by_id(id, contact_new)
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].id == id:
            old_contacts[i] = contact_new
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

# def test_edit_first_contact_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname = "test"))
#
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first_contact(Contact("new_fn"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts)  == len(new_contacts)