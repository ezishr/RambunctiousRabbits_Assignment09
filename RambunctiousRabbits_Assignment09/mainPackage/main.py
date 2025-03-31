# File Name : main.py
# Student Name: Peter Phan,
# email:  phanpv@mail.uc.edu, 
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
from DatabasePackage.databaseManagement import *
if __name__ == "__main__":
    dbm = DatabaseManagement()
    conn = dbm.connect_to_database()
    product_query = dbm.submit_sql_to_server(conn, 'SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct')
    product_query_result = product_query.fetchall()

    selected_row_number = 5
    product_id = product_query_result[0]
    product_description = product_query_result[2]
    manufacturer_id = product_query_result[3]
    brand_id = product_query_result[4]

    manufacturer_query = product_query.execute('''SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = ?''', (selected_row_number))
    for row in manufacturer_query:
        manufacturer_name = row
        print(manufacturer_name)

