# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()

    contact = Contact("fn", "mn", "ln", "nn", "t", "c", "address", "5", "6", "7", "8", "e1", "e2", "e3",
                               "www", "31", "May", "1234", "3", "July", "5678", "address", "6", "test")
    app.contact.create(contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)