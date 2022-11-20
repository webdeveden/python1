# this program will create table using sqlite and retrieve needed that by this python code

import sqlite3

conn = sqlite3.connect('exe15.sqlite')
cur = conn.cursor()#cursor() is like a database file handle.

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email= pieces[1]
    pos= email.split('@')
    org=pos[1]
    #print(org)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))# "?" it is placeholder for contents of the "org" variable.
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))# execute() it a methode we call in sql lite cursor object in python to run an sql command
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
# the executescript() methode in python SQLite cursor object allow multiple SQL statements separated by semicolons
