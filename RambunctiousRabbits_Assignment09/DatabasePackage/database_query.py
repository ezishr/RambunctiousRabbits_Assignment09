# File Name : database_query.py
# Student Name: Peter Phan
# email:  phanpv@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   04/03/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:   Develop a VS project to access a SQL server instance to extract some data
#                                        from Grocery Store Simulator database and produce interesting results. 

# Brief Description of what this module does. Learn about accessing a database and producing results from the data. 
# Citations: Stack Overflow: https://stackoverflow.com/questions/28981770/store-sql-result-in-a-variable-in-python
#            Stack Overflow: https://stackoverflow.com/questions/66512717/object-is-not-subscriptable-fix
#            Stack Overflow: https://stackoverflow.com/questions/37405287/using-python-variables-in-mysql-insert-statement
# Anything else that's relevant:

import pyodbc

class DatabaseManagement:
    def connect_to_Grocery_Store(self):
        """
        Connect to SQL server instance
        @return the connection object or None on failure
        """
        try: 
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                                  'Database=GroceryStoreSimulator;'
                                  'uid=IS4010Login;'
                                  'pwd=P@ssword2;')
        except:
            return None
        return conn

    def submit_query(self, conn, sql_statement):
        """
        Submit a SQL statement to our SQL Server 
        @param conn connection object: The connection object
        @param sql_statement String: The SQL to submit 
        @return The pyodbc cursor object that contains the query result
        """
        try:
            cursor = conn.cursor()
            cursor.execute(sql_statement)

        except:
            return None 
        return cursor

    