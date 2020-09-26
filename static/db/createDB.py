import sqlite3
from sqlite3 import Error
import os


APP_PATH = os.getcwd()
DB_PATH = (APP_PATH+"/webdb.bd") 


def createDB():
    cursor = con.cursor()
    try:
        cursor.execute("""
            CREATE TABLE user(
                name    VARCHAR  NOT NULL,
                mail    VARCHAR  NOT NULL,
                passwd  VARCHAR  NOT NULL,
                PRIMARY KEY (name, mail)

            );
        """)
    except Exception as e:
        print(e)

    try:
        cursor.execute("""
            CREATE TABLE course(
                name VARCHAR PRIMARY KEY NOT NULL
            );
        """)
    except Exception as e:
        print(e)
    
    try:
        cursor.execute ("""
            CREATE TABLE lesson(
                lvl INT PRIMARY KEY NOT NULL,
                name VARCHAR NOT NULL,
                done BIT NOT NULL,
                courName VARCHAR,
                FOREIGN KEY(courName) REFERENCES course(name)
            );
        """)
    except Exception as e:
            print(e)

    try:
        cursor.execute("""
            CREATE TABLE enrolled(
                usrName VARCHAR,
                courName VARCHAR,
                FOREIGN KEY(usrName) REFERENCES user(name),
                FOREIGN KEY(courName) REFERENCES course(name)
                );""")
    except Exception as e:
        print(e)
    
    finally:
        con.close()


def InsertTest():
    cursor = con.cursor()

    try:
        cursor.execute("""
            INSERT INTO user(name, mail, passwd)
            VALUES('prueba', 'prueba@prueba.com', 'prueba')
    
        """)
    except Exception as e:
        print (e)
    finally:
        con.commit()
        con.close()





if __name__ == "__main__":
    try:
        con = sqlite3.connect("webdb.db")
    except Error:
        print(Error)

    finally:
        InsertTest()
        
