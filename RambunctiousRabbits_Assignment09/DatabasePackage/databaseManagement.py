# File Name: databaseManagement.py
# Student Name: Peter Phan, Eirlys Vo, Nathan Sharpe
# email: phanpv@mail.uc.edu, vopq@mail.uc.edu, sharpenn@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/03/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Develop a VS project to access a SQL server instance to extract some data from Grocery Store Simulator database and produce interesting results. 
# Brief Description of what this module does: Learn about accessing a database and producing results from the data. 
# Citations: In class code examples
# Anything else that's relevant: N/A

from ast import Try
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
        @conn: connection object
        @sql_statement String: the SQL to submit
        @params String: the parameters to pass to the SQL statement
        @return: the pyodbc cursor
        """
        cursor = conn.cursor()
        if params:
            cursor.execute(sql_statement, params)
        else:
            cursor.execute(sql_statement)
        return cursor