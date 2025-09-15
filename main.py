# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

df_first_five = pd.read_sql(""" SELECT employeeNumber, lastName FROM employees; """, conn)

df_five_reverse = pd.read_sql(""" SELECT lastName, employeeNumber FROM employees; """, conn)

df_alias = pd.read_sql(""" SELECT lastName, employeeNumber AS ID FROM employees; """, conn)


df_executive = pd.read_sql(""" 
SELECT 
    employees.*,
        CASE jobTitle
            WHEN 'President' THEN 'Executive'
            WHEN 'VP Sales' THEN 'Executive'
            WHEN 'VP Marketing' THEN 'Executive'
            ELSE 'Non-Executive'
        END AS role
    FROM employees;
""", conn)   

df_name_length = pd.read_sql("""
SELECT lastName, LENGTH(lastName) AS name_length FROM employees;
""", conn)

df_short_title = pd.read_sql("""
SELECT SUBSTRING(jobTitle, 1, 2) AS short_title FROM employees;
""", conn)

sum_total_price = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS sum_total_price
    FROM orderdetails;
""", conn).squeeze("columns")

df_day_month_year = pd.read_sql("""
SELECT 
    orderDate,
    STRFTIME('%d', orderDate) AS day,
    STRFTIME('%m', orderDate) AS month,
    STRFTIME('%Y', orderDate) AS year
FROM orders;
""", conn)

conn.close()