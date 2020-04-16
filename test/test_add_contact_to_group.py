from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
import random

orm = ORMFixture(host = "192.168.64.2",name = "addressbook", user = "root_elena", password="elenka")

def test_add_contact_to_group(app, db):
    # собираем списки групп и контактов из БД, если они пусты, добавляем группу и контакт
    groups = db.get_group_list()
    contacts = db.get_contact_list()
    if len(groups) == 0:
        app.group.create(Group(name="vacant_group"))
    if len(contacts) == 0:
        app.contact.create(Contact(firstname="vacant_contact"))

    # собираем списки групп и контактов, отсутствующих в таблице связи групп и контактов через orm, если таковых нет, то создаем
    old_vacant_contacts = orm.get_vacant_contacts()
    old_vacant_groups = orm.get_vacant_groups()

    if len(old_vacant_groups) == 0:
        app.group.create(Group(name="vacant_group"))
        old_vacant_groups = orm.get_vacant_groups()

    if len(old_vacant_contacts) == 0:
        app.contact.create(Contact(firstname="vacant_contact"))
        old_vacant_contacts = orm.get_vacant_contacts()

    # добавляем первый свободный контакт в первую свободную группу
    app.contact.add_contact_to_group(old_vacant_contacts[0], old_vacant_groups[0])
    print("Контакт c id %s в группу с id %s успешно добавлен" % (old_vacant_contacts[0], old_vacant_groups[0]))

    # собираем списки групп и контактов, отсутствующих в таблице связи групп и контактов через orm, после добавления
    new_vacant_contacts = orm.get_vacant_contacts()
    new_vacant_groups = orm.get_vacant_groups()

    # проверяем, что список вакантных групп и контактов изменился на 1
    assert len(old_vacant_contacts) == len(new_vacant_contacts) +1
    assert len(old_vacant_groups) == len(new_vacant_groups) +1
