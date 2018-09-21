# Author: unutbu
# URL:    https://stackoverflow.com/a/5365533/3364859

import sqlite3
import re



def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

conn = sqlite3.connect(':memory:')
conn.create_function("REGEXP", 2, regexp)
cursor = conn.cursor()
cursor.execute('CREATE TABLE foo (bar TEXT)')
cursor.executemany('INSERT INTO foo (bar) VALUES (?)',[('aaa"test"',),('blah',)])
cursor.execute('SELECT bar FROM foo WHERE bar REGEXP ?',['"test"'])
data=cursor.fetchall()
print(data)

