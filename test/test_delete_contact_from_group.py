from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
import random

orm = ORMFixture(host = "192.168.64.2",name = "addressbook", user = "root_elena", password="elenka")

def test_delete_contact_to_group(app, db):
    # собираем списки групп и контактов из БД, если они пусты, добавляем группу и контакт
    groups = db.get_group_list()
    contacts = db.get_contact_list()
    if len(groups) == 0:
        app.group.create(Group(name="dealed_group"))
    if len(contacts) == 0:
        app.contact.create(Contact(firstname="dealed_contact"))

    # собираем список контактов, присутствующих в таблице связи групп и контактов через orm, если таковых нет, то создаем и добавляем
    old_dealed_contacts = orm.get_dealed_contacts()

    # если нет занятого контакта, то создаю контакт и группу и связываю их, можно было бы выбрать из свободных групп, но не стала
    if len(old_dealed_contacts) == 0 :
        dealed_group = app.group.create(Group(name="dealed_group"))
        dealed_contact = app.contact.create(Contact(firstname="dealed_contact"))
        # app.contact.add_contact_to_group(old_vacant_contacts[0], old_vacant_groups[0])
        app.contact.add_contact_to_group( dealed_contact, dealed_group)
        old_dealed_contacts = orm.get_dealed_contacts()

    dealed_contact = old_dealed_contacts[0]
    dealed_group = orm.get_groups_of_contact(dealed_contact)[0]

    app.contact.remove_contact_from_group(dealed_contact, dealed_group)
    print("Контакт c id %s из группы с id %s успешно удален" % (dealed_contact, dealed_group))

    # собираем списки групп и контактов, отсутствующих в таблице связи групп и контактов через orm, после добавления
    new_dealed_contacts = orm.get_dealed_contacts()

    # проверяем, что список вакантных контактов изменился на 1 (считаю, что контакт может быть только в одной группе)
    assert len(old_dealed_contacts) == len(new_dealed_contacts) +1