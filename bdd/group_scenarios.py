from pytest_bdd import scenario
from .group_steps import *

# запускатели тестов

@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass

@scenario('groups.feature', 'Delete a group')
def test_delete_some_group():
    pass

@scenario('groups.feature', 'Modify a group')
def test_modify_some_group():
    pass