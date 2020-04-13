from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
import random

orm = ORMFixture(host = "192.168.64.2",name = "addressbook", user = "root_elena", password="elenka")

def test_add_contact_to_group(app, db):
    # собираем списки групп и контактов из БД
    groups = db.get_group_list()
    contacts = db.get_contact_list()
    contacts_in_group = []
    contact_is_real = Contact()
    group_is_real = Group()

    if len(groups) == 0:
        app.group.create(Group(name="test_group"))
        groups = db.get_group_list()
    if len(contacts)== 0:
        app.contact.create(Contact(firstname = "test_firstname"))
        contacts = db.get_contact_list()

    # проверка, пробегаемся по группам - ищем первый контакт из списка контактов, принадлежащего заданной группе
    for g in range(len(groups)):
        contacts_in_group = orm.get_contacts_in_group(Group(id=str(groups[g].id)))
        if len(contacts_in_group) != 0:
            contact_is_real = contacts_in_group[0]
            group_is_real = groups[g]
            break
    # если не нашлось контактов, принадлежащих хоть какой-то группе, добавим первый контакт в первую группу и удалим
    if len(contacts_in_group) == 0:
        app.contact.add_contact_to_group(contacts[0], groups[0])
        app.contact.remove_contact_from_group(contacts[0], contacts[0])
        print("Контакт c id %s из группы с id %s успешно удален" % (contacts[0].id, group_is_real.id))
    else:
        app.contact.remove_contact_from_group(contact_is_real, group_is_real)
        print("Контакт c id %s из группы с id %s успешно удален" % (contact_is_real.id, group_is_real.id))
