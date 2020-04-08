# -*- coding: utf-8 -*-
from model.contact import Contact
import  random

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname = "test"))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

   # для отключаемой проверки, где сраниваем БД инфу с UI, надо преобразовать список, взятый из БД, - взять только id и name
    if check_ui:
        new_contacts_ui = []
        for i in new_contacts:
          new_contacts_ui.append(Contact(id = i.id,
                                         all_phones_from_home_page = app.contact.merge_phones_like_on_home_page(i),
                                         all_emails_from_home_page = app.contact.merge_emails_like_on_home_page(i),
                                         firstname = app.contact.clear_extra_spaces(i.firstname),
                                         lastname = app.contact.clear_extra_spaces(i.lastname),
                                         address = app.contact.clear_extra_spaces(i.address)
                                         )
                                 )
        assert sorted(new_contacts_ui, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max)