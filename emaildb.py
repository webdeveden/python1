import sqlite3 #import the sqllite library

conn = sqlite3.connect('emaildb.sqlite')# making a connection , emaildb.sqlite is a file
cur = conn.cursor()# cursor is like a file handle

cur.execute('DROP TABLE IF EXISTS Counts')# drop table if it exist (if the emaildb.sqlite file exist), if not ...

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')# create a table,table name= counts ,row and colums

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))# the ? is a place holder in sql ,so we use this to avoid sql injection
    row = cur.fetchone()# grab the first one
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))# if not that email in the table ,create it as a new email and make count=1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))# if there only update count by adding 1 on it
    conn.commit()# writting out those command from database memory

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'# selecting the email descending and only the top 10

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])# row[0]= email and row[1]= count

cur.close()
