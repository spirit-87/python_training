from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
import random

orm = ORMFixture(host = "192.168.64.2",name = "addressbook", user = "root_elena", password="elenka")

def test_add_contact_to_group(app, db):
    # собираем списки групп и контактов из БД
    groups = db.get_group_list()
    contacts = db.get_contact_list()

    # проверка, пробегаемся по группам - ищем первый контакт из списка контактов, не принадлежищего заданной группе
    for g in range(len(groups)):
        contacts_not_in_group = orm.get_contacts_not_in_group(Group(id=str(groups[g].id)))
        if len(contacts_not_in_group) != 0:
            contact_is_real = contacts_not_in_group[0]
            group_is_real = groups[g]
            break
    if len(contacts_not_in_group) == 0:
        app.group.create(Group(name="test"))
        groups = db.get_group_list()
        group_is_real = groups[0]
        app.contact.add_contact_to_group(contacts[0], group_is_real)
        print("Контакт c id %s в группу с id %s успешно добавлен" % (contacts[0].id, group_is_real.id))
    else:
        app.contact.add_contact_to_group(contact_is_real, group_is_real)
        print("Контакт c id %s в группу с id %s успешно добавлен" % (contact_is_real.id, group_is_real.id))

