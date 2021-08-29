import sqlite3

def test():
    # Connect to database
    conn = connect()
    # Create a table
    createTable(conn)
    # Insert some records in to the table
    insertRecords(conn)
    # Read records from table
    readRecords(conn)

def connect():
    return sqlite3.connect('test_hr.db')

def createTable(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS USER (
                            ID INT PRIMARY KEY NOT NULL,
                            NAME TEXT NOT NULL,
                            SALARY REAL
                        );
                ''')

def insertRecords(conn):
    conn.execute('''
                    INSERT INTO USER(ID,NAME,SALARY) VALUES (1000,'HIMANSHU',100000.00)
                ''')
    conn.execute('''
                    INSERT INTO USER(ID,NAME,SALARY) VALUES (2000,'Heena',200000.00)
                ''')
    conn.execute('''
                    INSERT INTO USER(ID,NAME,SALARY) VALUES (3000,'Sambit',300000.00)
                ''')

def readRecords(conn):
    cursor = conn.execute('SELECT * FROM USER')
    for record in cursor:
        print('ID : {}'.format(record[0]))
        print('NAME : {}'.format(record[1]))
        print('SALARY : {}'.format(record[2]))
        print('--------------------------')
