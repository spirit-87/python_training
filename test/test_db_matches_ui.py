from model.group import Group
import re
from timeit import timeit

def test_group_list(app, db):

    def clean(group):
        return Group(id = group.id, name = re.sub("  ", " ", group.name.strip()))

    ui_list = map(clean, app.group.get_group_list())
    db_list = map(clean, db.get_group_list())

    print(timeit(lambda:ui_list, number=1 ))
    print(timeit(lambda:db_list, number=1000 ))

    assert sorted(ui_list, key = Group.id_or_max) == sorted(db_list, key = Group.id_or_max)

