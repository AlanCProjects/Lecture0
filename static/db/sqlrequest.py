import sqlite3
from sqlite3 import Error
import os


def sqlselect(table, row = "*", condition = ""):
    lst = []
    conn = sqlite3.connect("./static/db/webdb.db")
    cursor = conn.cursor()
    if (condition == ""):
        try:
            cursor.execute(f"""
                SELECT {row}
                FROM {table}
            
            """)
        except Exception as e:
            raise e
    else:
        try:
            cursor.execute(f"""
            SELECT {row}
            FROM {table}
            WHERE {condition}
            """)
        except Exception as e:
            raise e
        
    rows = cursor.fetchall()
    for row in rows:
        lst.append(str(row).strip(",'()"))

    conn.close()

    return lst

def sqlinsert(name, mail, passwd):
    
    conn = sqlite3.connect("./static/db/webdb.db")
    cursor = conn.cursor()

    try:    
        cursor.execute(f"""
            INSERT INTO user(name, mail, passwd)
            VALUES('{name}', '{mail}', '{passwd}')
        """)
        conn.commit()
    except Exception as e:
        raise e

    conn.close()