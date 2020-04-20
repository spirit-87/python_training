from pytest_bdd import given, when, then
from model.group import Group
import random

# given - фикстуры, поэтому их можно передавать в другие тесты
@given('a group list')
def group_list(db):
    return db.get_group_list()

@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name = name, header = header, footer = footer)

@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then('the new group list is equal to the old list with added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(new_group)
    return db.get_group_list()

@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@then('new list is equal to the old list without the deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups) + 1
    old_groups.remove(random_group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

@given('a group with <name_mod>, <header_mod> and <footer_mod>')
def mod_group(name_mod,  header_mod, footer_mod, app):
    return Group(name = app.group.clear_extra_spaces(name_mod), header= app.group.clear_extra_spaces(header_mod),
                   footer = app.group.clear_extra_spaces(footer_mod))

@when('I modify the group from the list')
def modify_group(app, random_group, mod_group):
    app.group.edit_group_by_id(random_group.id, mod_group)

@then('new list is equal to the old list with the modified group')
def verify_group_modified(db, non_empty_group_list, random_group, mod_group):
    old_groups = non_empty_group_list
    mod_group.id = random_group.id
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == mod_group.id:
            old_groups[i] = mod_group

    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)






