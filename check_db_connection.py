import pymysql.cursors
#from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group
#connection = pymysql.connect(host = "192.168.64.2",database = "addressbook", user = "root_elena", password="elenka")
db = ORMFixture(host = "192.168.64.2",name = "addressbook", user = "root_elena", password="elenka")
try:

    # l = db.get_group_list()
    # for item in l:
    #     print(item)
    # print(len(l))

    l = db.get_contacts_not_in_group(Group(id = '55'))
    for item in l:
        print(item)
    print(len(l))

finally:
    #connection.close()
    #db.destroy()
    pass