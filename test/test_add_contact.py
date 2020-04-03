# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(maxlen):
    digits = string.digits
    return "".join([random.choice(digits) for i in range(maxlen)])

testdata =  [Contact(
            firstname = "", middlename = "", lastname = "",
            nickname = "",
            title = "", company = "",
            address = "", phone_home = "",
            phone_mobile = "", phone_work = "", phone_fax = "",
            email1 = "", email2 = "", email3 = "",
            webpage = "",
            byear = "", ayear = "", address2 = "",
            phone2 = "", notes2 = "")] + [
            Contact(
            firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 10),
            phone_home=random_phone(7), phone_mobile=random_phone(7), phone_work=random_phone(7), phone_fax=random_phone(7),
            email1=random_string("email1", 10), email2=random_string("email2", 10), email3=random_string("email3", 10),
            webpage=random_string("title", 10),
            byear=random_string("", 4),
            ayear=random_string("", 4),
            address2=random_string("address2", 10), phone2=random_phone(7), notes2=random_string("notes2", 10))
            for i in range(5)
            ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()

    app.contact.create(contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)