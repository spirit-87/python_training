# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "test"))

    old_contacts = app.contact.get_contact_list()

    contact = Contact("fn", "mn", "ln", "nn", "t", "c", "address", "5", "6", "7", "8", "e1", "e2", "e3",
                "www", "31", "May", "1234", "3", "July", "5678", "address", "6", "test")
    contact.id = old_contacts[0].id

    app.contact.edit_first_contact(contact)

    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)  == len(new_contacts)
    old_contacts[0]=contact
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

# def test_edit_first_contact_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname = "test"))
#
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first_contact(Contact("new_fn"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts)  == len(new_contacts)