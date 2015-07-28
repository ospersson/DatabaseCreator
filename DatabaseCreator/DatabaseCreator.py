import sqlite3 as lite
import sys

con = None

"""
Read and execute SQL statements from file.
"""
def executeSqlFile(dbPathName, dbFileName): 
    print('Start executing sql statements')
    
    with open(dbPathName + '\\' + dbFileName, mode = 'r', encoding="utf8") as f:
        for line in f:
            if 'GO' in line:
                con.commit()
            elif line == '\n':
                pass
            else:
                cur.execute(line)

    print('End executing values')

"""
List all rows from a table
"""
def printTable(tableName):
    cur.execute('SELECT * FROM ' + tableName)
    rows = cur.fetchall()

    print('\n')
    for row in rows:
        print(row)

    print('\n')

try:
    sqlFilePath = 'c:\\temp'
    dbName = 'buildings.db'

    con = lite.connect(dbName)
    cur = con.cursor()

    executeSqlFile(sqlFilePath, 'createDb.sql')
    executeSqlFile(sqlFilePath, 'buildings.sql')
    printTable('Buildings')
    printTable('City')

except lite.Error as e:
    if con:
        con.rollback()

    print ("Error: ", e.args[0])
    sys.exit(1)
    
finally:
    if con:
        con.close()

