from model.contact import Contact
import random
import string

constant = [Contact(
            firstname = "firstname1", middlename = "middlename1", lastname = "lastname1",
            nickname = "nickname1",
            title = "title1", company = "company1",
            address = "address1", phone_home = "111",
            phone_mobile = "122", phone_work = "133", phone_fax = "144",
            email1 = "e11", email2 = "e21", email3 = "e31",
            webpage = "webpage1",
            byear = "", ayear = "", address2 = "address21",
            phone2 = "155", notes2 = "notes21"),
            Contact(
                firstname="firstname2", middlename="middlename2", lastname="lastname2",
                nickname="nickname2",
                title="title2", company="company2",
                address="address2", phone_home="211",
                phone_mobile="222", phone_work="233", phone_fax="244",
                email1="e12", email2="e22", email3="e32",
                webpage="webpage2",
                byear="", ayear="", address2="address22",
                phone2="255", notes2="notes22"),
            ]

def random_phone(maxlen):
    digits = string.digits
    return "".join([random.choice(digits) for i in range(maxlen)])


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

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