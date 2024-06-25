"""
DOC: https://memcached.org/
brew install memcached

memcached -vv
"""

import sqlite3
import memcache

db = memcache.Client(['127.0.0.1:11211'])

# db.set('web_page', 'value1')
# print(db.get('web_page'))

# db.set('counter', 0)
# db.incr('counter', 1)

conn = sqlite3.connect('test_sqlite2.db')
curs = conn.cursor()
# curs.execute(
#     'CREATE TABLE persons('
#     'employee_id INTEGER PRIMARY KEY AUTOINCREMENT , name STRING)')
# curs.execute('INSERT INTO persons(name) values("Mike")')
# conn.commit()
# conn.close()

def get_employee_id(name):
    employee_id = db.get(name)
    if employee_id:
        return employee_id
    curs.execute(f'SELECT * FROM persons WHERE name = "{name}"')
    person = curs.fetchone()
    if not person:
        raise Exception('No employee')
    employee_id, name = person
    db.set(name, employee_id, time=60)
    return employee_id

print(get_employee_id('Mike'))
    
