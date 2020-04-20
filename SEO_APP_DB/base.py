from os import path
#from queries import *
import sqlite3
from sqlite3 import Error


BASE_PATH = path.dirname(path.abspath(__file__))
RELATIVE_PATH = BASE_PATH + '/Scripts/Select_query.sql'
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn, query):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows: print(row)


def main():
    database = r"/Users/albi/Library/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db"

    conn = create_connection(database)
    cur = conn.cursor()
    result = cur.execute('select FirstName from Customer')

    with create_connection(database) as ConnectionSL:
        con2 = ConnectionSL.cursor()
        res = con2.execute('select FirstName from Customer')

        for i in res:
            print(i)
        #query = SqlLiteQuery().from_file(RELATIVE_PATH)
        #ress = con2.execute(query)
        #for res in ress: print(res)
    ConnectionSL.commit()
    ConnectionSL.close()
if __name__ == '__main__':
    main()