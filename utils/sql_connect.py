import pyodbc
import keyring

class Sql_Connect():

    def __init__(self, server, database, user):

        self.server = server
        self.database = database
        self.user = user

        self.conn, self.cursor = self.connect()

    def connect(self):
        
        password = keyring.get_password(self.database, self.user)

        connect_string = f"""Driver={{ODBC Driver 17 for SQL Server}};Server={self.server};Database={self.database};uid={self.user};pwd={password};"""
        conn = pyodbc.connect(connect_string)

        return conn, conn.cursor()

    def get_columns(self, table):
        
        query = f"""SELECT COLUMN_NAME, DATA_TYPE
                  FROM INFORMATION_SCHEMA.COLUMNS
                  WHERE TABLE_NAME = ?
                  ORDER BY ORDINAL_POSITION"""
        
        self.cursor.execute(query, (table))
        return self.cursor.fetchall()


    def execute(self, sql):
        
        self.cursor.execute(sql, (table))


    def insert(self, df, table):
        insert_string = 'INSERT INTO {0} VALUES ('.format(table)
        insert_string = insert_string + (df.shape[1]-1) * '?,' + '?)'

        self.cursor()
    def __del__(self):
        self.cursor.close()
        self.conn.close()



