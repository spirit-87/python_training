# -*- coding: utf-8 -*-
from model.contact import Contact
import  random

def test_delete_first_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname = "test"))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
