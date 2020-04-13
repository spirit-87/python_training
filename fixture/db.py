import pymysql
from model.group import Group
from model.contact import Contact
import re

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host,
        self.name = name,
        self.user = user,
        self.password = password,
        self.connection = pymysql.connect(host = host,database = name, user = user, password=password, autocommit = True)
# autocommit убирает кэширование в базе, чтобы после изменений в проверках обновлялось кол-во групп

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id = str(id), name = name, header = header, footer = footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                current_contact = Contact(id = str(id), firstname = firstname, lastname = lastname, address = address,
                                          phone_home = home, phone_mobile = mobile, phone_work = work, phone2 = phone2,
                                          email1 = email, email2 = email2, email3 = email3
                                            )
                final_contact = Contact(id = str(id), firstname = self.clear_extra_spaces(firstname),
                                        lastname = self.clear_extra_spaces(lastname),
                                        address = self.clear_extra_spaces(address)
                                        )
                final_contact.all_phones_from_home_page = self.merge_phones_like_on_home_page(current_contact)
                final_contact.all_emails_from_home_page = self.merge_emails_like_on_home_page(current_contact)
                list.append(final_contact)

        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def clear(self, s):
        return re.sub("[()-]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        #filter - удаляем элементы None, map - чистим контакты от лишних символов, filter - выбираем только не пустые значения
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x).strip(),
                                    filter(lambda x: x is not None,
                                           [contact.phone_home, contact.phone_mobile, contact.phone_work, contact.phone2]))))

    def merge_emails_like_on_home_page(self, contact):
    #filter - удаляем элементы None, map - чистим контакты от лишних символов, filter - выбираем только не пустые значения
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x:self.clear(x).strip(),
                                    filter(lambda x: x is not None,
                                           [contact.email1, contact.email2, contact.email3]))))

    def clear_extra_spaces(self, s):
        return re.sub("  ", " ", s.strip())