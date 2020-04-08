# -*- coding: utf-8 -*-
from model.contact import Contact
import re

#def test_add_contact(app, data_contacts): - если хотим грузить константные данные из заранее заготовленного файла
#def test_add_contact(app, json_contacts): - если хотим грузить сгенерированные в отдельном файле данные

def test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
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

