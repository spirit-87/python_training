from model.contact import Contact
import os.path
import random
import string
import json
import getopt
import sys
import jsonpickle

# n - кол-во загружаемых данных, f  - файл, куда данные должны помещаться
# чтение опций из командной строки
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
            for i in range(n)
            ]
# ".." - переход на 1 уровень вверх (в корневую директорию проекта)
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file,"w") as out:
    #out.write(json.dumps(testdata, default = lambda x: x.__dict__, indent=2))
    out.write(jsonpickle.encode(testdata))



