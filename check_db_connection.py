import pymysql.cursors
from fixture.db import DbFixture

#connection = pymysql.connect(host = "192.168.64.2",database = "addressbook", user = "root_elena", password="elenka")
db = DbFixture(host = "192.168.64.2",name = "addressbook", user = "root_elena", password="elenka")
try:
    # cursor = connection.cursor() # курсор на данные из БД
    # cursor.execute("SELECT * FROM group_list") # обычный sql запрос
    # for row in cursor.fetchall(): # fetchall - возвращает все, то извлеклось из БД, в виде набора строк
    #     print(row)

    # groups = db.get_group_list()
    # for group in groups:
    #     print(group)
    # print(len(groups))

    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))

finally:
    #connection.close()
    db.destroy()