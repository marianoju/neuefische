# Author: JOHN_16 
# URL:    https://stackoverflow.com/a/50066799/3364859

import sqlite3
import re


def functionRegex(value, pattern):
    c_pattern = re.compile(r"\b" + pattern.lower() + r"\b")
    return c_pattern.search(value) is not None

connection = sqlite3.connect(':memory:')
cur = connection.cursor()

cur.execute('CREATE TABLE tweet(msg TEXT)')
cur.execute('INSERT INTO tweet VALUES("This is a test message")')
cur.execute('INSERT INTO tweet VALUES("Another message")')

connection.create_function("REGEXP", 2, functionRegex)

print(cur.execute('SELECT * FROM tweet WHERE REGEXP(msg, ?)', ('test',)).fetchall())
print(cur.execute('SELECT * FROM tweet WHERE REGEXP(msg, ?)', ('message',)).fetchall())
print(cur.execute('SELECT * FROM tweet WHERE ? REGEXP msg', ('message',)).fetchall())

