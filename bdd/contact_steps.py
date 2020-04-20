from pytest_bdd import given, when, then
from model.contact import Contact
import random

# given - фикстуры, поэтому их можно передавать в другие тесты
@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <firstname>, <lastname> and <address>')
def new_contact(firstname, lastname, address, app):
    return Contact(firstname = app.contact.clear_extra_spaces(firstname), lastname= app.contact.clear_extra_spaces(lastname),
                   address = app.contact.clear_extra_spaces(address))

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@then('the new contact list is equal to the old list with added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(new_contact)
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('new list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts)- 1  == new_contacts
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

@given('a contact with <firstname_mod>, <lastname_mod> and <address_mod>')
def mod_contact(firstname_mod, lastname_mod, address_mod, app):
    return Contact(firstname = app.contact.clear_extra_spaces(firstname_mod), lastname= app.contact.clear_extra_spaces(lastname_mod),
                   address = app.contact.clear_extra_spaces(address_mod))

@when('I modify the contact from the list')
def modify_contact(app, random_contact, mod_contact):
    app.contact.edit_contact_by_id(random_contact.id, mod_contact)

@then('new list is equal to the old list with the modified contact')
def verify_contact_modified(db, non_empty_contact_list, random_contact, mod_contact):
    old_contacts = non_empty_contact_list
    mod_contact.id = random_contact.id
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].id == mod_contact.id:
            old_contacts[i] = mod_contact

    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)



