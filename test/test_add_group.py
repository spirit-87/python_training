# -*- coding: utf-8 -*-
from model.group import Group



# Разделили тестовые данные и операции с ними
# Добавили генерацию случайных данных
# Добавили множ-во тестов со случ. данными


#def test_add_group(app, data_groups): - если хотим грузить константные данные из заранее заготовленного файла
#def test_add_group(app, json_groups): - если хотим грузить сгенерированные в отдельном файле данные
def test_add_group(app, db, json_groups):
    #pass
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    # для сортировки нужен ключ, если у группы нет id, то непонятно, как сортировать, но новая группа должна быть на последнем месте
    # и иметь самый большой id
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
