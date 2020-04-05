from model.group import Group
import os.path
import random
import string
import json
import getopt
import sys
import jsonpickle

# n - кол-во загружаемых данных, f  - файл, куда данные должны помещаться
# чтение опций из командной строки
# -n10 -f"data/test1.json"
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [
            Group(name=random_string("name", 10), header=random_string("header", 10),
                  footer=random_string("footer", 10))
            for i in range(n)
           ]
# ".." - переход на 1 уровень вверх (в корневую директорию проекта)
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    # jsonpickle добавляет в json данные ключ: указывающий на класс исходных данных
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

