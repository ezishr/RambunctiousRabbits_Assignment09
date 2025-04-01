# File Name: main.py
# Student Name: Peter Phan, Eirlys Vo, Nathan Sharpe
# email: phanpv@mail.uc.edu, vopq@mail.uc.edu, sharpenn@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/03/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Develop a VS project to access a SQL server instance to extract some data from Grocery Store Simulator database and produce interesting results. 
# Brief Description of what this module does: Learn about accessing a database and producing results from the data. 
# Citations: Stack Overflow: https://stackoverflow.com/questions/28981770/store-sql-result-in-a-variable-in-python
#            Stack Overflow: https://stackoverflow.com/questions/66512717/object-is-not-subscriptable-fix
#            Stack Overflow: https://stackoverflow.com/questions/37405287/using-python-variables-in-mysql-insert-statement
# Anything else that's relevant: N/A

from DatabasePackage.databaseManagement import *
import random

if __name__ == "__main__":
    dbm = DatabaseManagement()

    conn = dbm.connect_to_database()
    product_query = dbm.submit_sql_to_server(conn, 'SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct')
    product_query_result = product_query.fetchall()


    selected_row_number = random.randint(0, len(product_query_result) - 1)
    selected_row_data = product_query_result[selected_row_number]

    product_description = selected_row_data[2]

    product_id = selected_row_data[0]

    manufacturer_id = selected_row_data[3]

    brand_id = selected_row_data[4]

    # Submit query to get the Manufacturer name from row 5
    manufacturer_query = dbm.submit_sql_to_server(conn, 'SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = ?', (manufacturer_id,))
    # Fetch the first Manufactere name if exists  
    manufacturer_result = manufacturer_query.fetchone()
    manufacturer_name = manufacturer_result[0] if manufacturer_result else "Unknown Manufacturer"


    # Submit query to get the Brand name from row 5
    brand_query = dbm.submit_sql_to_server(conn, 'SELECT Brand FROM tBrand WHERE BrandID = ?', (brand_id,))
    # Fetch the first Brand name if exists
    brand_result = brand_query.fetchone()
    brand_name = brand_result[0] if brand_result else "Unknown Brand"
   
    # Substitute product ID into query from step 2
    substituted_product_query = dbm.submit_sql_to_server(conn, 'SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold FROM dbo.tTransactionDetail INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = ?)', (product_id,))
    
    number_of_items_sold = substituted_product_query.fetchone()[0]
    
    # Print statement
    print(f'Product Description: {product_description}, Manufacturer: {manufacturer_name}, Brand: {brand_name}, Number of Items Sold: {number_of_items_sold}')