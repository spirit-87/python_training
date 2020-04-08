import re
from random import randrange

def test_phones_on_homepage(app):
    index = randrange(len(app.contact.get_contact_list()))

    contact_from_homepage = app.contact.get_contact_list()[index] #контакт из списка
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(index)  # контакт из формы редактирования

    assert contact_from_homepage.firstname == contact_from_editpage.firstname
    assert contact_from_homepage.lastname == contact_from_editpage.lastname
    assert contact_from_homepage.address == contact_from_editpage.address
    # assert contact_from_homepage.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_editpage)
    # assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_editpage)
    assert contact_from_homepage.all_emails_from_home_page == contact_from_editpage.all_emails_from_home_page
    assert contact_from_homepage.all_phones_from_home_page == contact_from_editpage.all_phones_from_home_page


# def test_phones_on_contact_view_page(app):
#     contact_from_viewpage = app.contact.get_contact_info_from_view_page(0) #контакт из viewpage контакта
#     contact_from_editpage = app.contact.get_contact_info_from_edit_page(0) #контакт из формы редактирования
#     assert contact_from_viewpage.phone_home == contact_from_editpage.phone_home
#     assert contact_from_viewpage.phone_mobile == contact_from_editpage.phone_mobile
#     assert contact_from_viewpage.phone_work == contact_from_editpage.phone_work
#     assert contact_from_viewpage.phone2 == contact_from_editpage.phone2

def clear(s):
    return re.sub("[() -]", "", s)

# def merge_phones_like_on_home_page(contact):
#     #filter - удаляем элементы None, map - чистим контакты от лишних символов, filter - выбираем только не пустые значения
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x:clear(x),
#                                 filter(lambda x: x is not None,
#                                        [contact.phone_home, contact.phone_mobile, contact.phone_work, contact.phone2]))))
#
# def merge_emails_like_on_home_page(contact):
#     #filter - удаляем элементы None, map - чистим контакты от лишних символов, filter - выбираем только не пустые значения
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x:clear(x),
#                                 filter(lambda x: x is not None,
#                                        [contact.email1, contact.email2, contact.email3]))))
#
