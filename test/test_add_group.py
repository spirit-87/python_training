# -*- coding: utf-8 -*-
from model.group import Group
import re
import pytest



# Разделили тестовые данные и операции с ними
# Добавили генерацию случайных данных
# Добавили множ-во тестов со случ. данными


#def test_add_group(app, data_groups): - если хотим грузить константные данные из заранее заготовленного файла
#def test_add_group(app, json_groups): - если хотим грузить сгенерированные в отдельном файле данные
def test_add_group(app, db, check_ui, json_groups):
    #pass
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('When I add the group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new group list is equal to the old list with added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        # для сортировки нужен ключ, если у группы нет id, то непонятно, как сортировать, но новая группа должна быть на последнем месте
        # и иметь самый большой id
        assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

        # для отключаемой проверки, где сраниваем БД инфу с UI, надо преобразовать список, взятый из БД, - взять только id и name
        if check_ui:
            new_groups_ui = []
            for i in new_groups:
                new_groups_ui.append(Group(id=i.id, name=re.sub("  ", " ", i.name.strip())))
            assert sorted(new_groups_ui, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)
