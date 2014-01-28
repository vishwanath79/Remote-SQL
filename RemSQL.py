#!/usr/bin/python
import MySQLdb
import prettytable
from prettytable import from_db_cursor
host = raw_input('Enter host name ')
user = raw_input('Enter username ')
passwd = raw_input('Enter password ')
database = raw_input('Enter DB ')
db = MySQLdb.connect(host, # your host, usually localhost
                     user, # your username
                      passwd, # your password
                      database) # name of the data base)

# Create a Cursor object
cur = db.cursor() 
col = raw_input('Enter Column Name')
table = raw_input('Enter Table name')
#columns = map(col, col.split())
cur.execute("SELECT "+col+" FROM "+database+ "."+table+"")
pt = from_db_cursor(cur)
print pt
cur.close()