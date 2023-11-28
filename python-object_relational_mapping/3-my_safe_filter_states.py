#!/usr/bin/python3
"""protect from SQL injection by using parameterised queries"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    state_name_searched = sys.argv[4]
    query = """SELECT * FROM states WHERE BINARY name = %s ORDER BY id;"""
    tpl = (state_name_searched,)
    cur.execute(query, tpl)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
