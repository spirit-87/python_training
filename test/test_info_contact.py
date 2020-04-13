from model.contact import Contact
from random import randrange

def test_contacts_on_homepage(app, db):
    contacts_from_homepage = sorted(app.contact.get_contact_list(),  key = Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(),  key = Contact.id_or_max)
    assert len(contacts_from_homepage) == len(contacts_from_db)

    for i in range(len(contacts_from_homepage)):
        assert contacts_from_homepage[i].firstname == contacts_from_db[i].firstname
        assert contacts_from_homepage[i].lastname == contacts_from_db[i].lastname
        assert contacts_from_homepage[i].address == contacts_from_db[i].address
        assert contacts_from_homepage[i].all_phones_from_home_page == contacts_from_db[i].all_phones_from_home_page
        assert contacts_from_homepage[i].all_emails_from_home_page == contacts_from_db[i].all_emails_from_home_page



# def test_phones_on_contact_view_page(app):
#     contact_from_viewpage = app.contact.get_contact_info_from_view_page(0) #контакт из viewpage контакта
#     contact_from_editpage = app.contact.get_contact_info_from_edit_page(0) #контакт из формы редактирования
#     assert contact_from_viewpage.phone_home == contact_from_editpage.phone_home
#     assert contact_from_viewpage.phone_mobile == contact_from_editpage.phone_mobile
#     assert contact_from_viewpage.phone_work == contact_from_editpage.phone_work
#     assert contact_from_viewpage.phone2 == contact_from_editpage.phone2

