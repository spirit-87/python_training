import pymysql.cursors
connection = pymysql.connect(host = "192.168.64.2",database = "addressbook", user = "root_elena", password="elenka")

try:
    cursor = connection.cursor() # курсор на данные из БД
    cursor.execute("SELECT * FROM group_list") # обычный sql запрос
    for row in cursor.fetchall(): # fetchall - возвращает все, то извлеклось из БД, в виде набора строк
        print(row)
finally:
    connection.close()