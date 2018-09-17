#
# Pre-requisites:
# Python2.5+ with sqlite3  - pysqlite is available in your python installation (included in the standard library since Python 2.5)
#
# This script will print 10 rows from teams and users table
#


import sqlite3 # assumes you already have sqlite3 
 

def main():

    db = sqlite3.connect('movies.db')
    cursor = db.cursor()

    for row in cursor.execute('SELECT * from movies'):
      print(row)

    for row in cursor.execute('SELECT * from actors'):
      print(row)


if __name__ == '__main__':
    main()
