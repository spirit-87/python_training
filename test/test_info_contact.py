from model.contact import Contact
from random import randrange

def test_phones_on_homepage(app, db):
    contacts_from_homepage = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert sorted(contacts_from_homepage, key = Contact.id_or_max) == sorted(contacts_from_db, key = Contact.id_or_max)


# def test_phones_on_contact_view_page(app):
#     contact_from_viewpage = app.contact.get_contact_info_from_view_page(0) #контакт из viewpage контакта
#     contact_from_editpage = app.contact.get_contact_info_from_edit_page(0) #контакт из формы редактирования
#     assert contact_from_viewpage.phone_home == contact_from_editpage.phone_home
#     assert contact_from_viewpage.phone_mobile == contact_from_editpage.phone_mobile
#     assert contact_from_viewpage.phone_work == contact_from_editpage.phone_work
#     assert contact_from_viewpage.phone2 == contact_from_editpage.phone2

