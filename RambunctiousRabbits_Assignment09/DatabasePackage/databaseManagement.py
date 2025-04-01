# databaseManagement.py
from ast import Try
from calendar import c
import pyodbc

class DatabaseManagement:
    def connect_to_database(self):
        """
        Connect to our SQL Server instance
        @return the connection object or None on failure
        """

        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                              'Database=GroceryStoreSimulator;'
                              'uid=IS4010Login;'
                              'pwd=P@ssword2;')
            return conn

        except:
            print('Unable to connect to database')
            return None


    def submit_sql_to_server(self, conn, sql_statement, params = None):
        """
        Submit a SQL statement to SQL Server
        @param conn: connection object
        @param sql_statement String: the SQL to submit
        @return: the pyodbc cursor
        """
        cursor = conn.cursor()
        if params:
            cursor.execute(sql_statement, params)
        else:
            cursor.execute(sql_statement)
        return cursor