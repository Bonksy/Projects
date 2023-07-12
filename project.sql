/*  Project: Customers and Products Analysis Using SQL

Welcome to my project where I will be conducting data analysis on a scale model car database to extract KPI's
in order to make smarter decisions.

Durign this project there are three questions we want to as ourselves.

Question 1: Which products should we order more of or less of?
Question 2: How should we tailor marketing and communication strategies to customer behaviors?
Question 3: How much can we spend on acquiring new customers?

Within the clase model car database we will be working with 8 tables.

The tables are as follows:

1. productslines table - this table contains product category data containing 4 columns. The product line is the primary key. This table
has a relationship with the producttable on the product line column which is a one-to-many relationship.

2. products table - this table contains product data. This table has 9 columns. The productCode is the primary key and productLine the 
foreign key. This table has a relationship with the productlines table on the productLine column which is a many-to-one relationship
and the orderdetails table on the productCode column which is a one-to-one relationship.

3. orderdetails table - this table contains order details data. This table has 5 columns. The orderNumber & productCode are the composite 
key. This table has a relationship with the products table productCode colum which is a one-to-one relationship and the order table on the
orderNumber column which is a one-to-one relationship.

4. orders table - this table contains orders recieved data. This table has 7 columns.The orderNumber is the primary key.
and the customerNumber is the foreign key. This table has a relationship with the orderdetails table on the orderNumber table which is
a one-to-one relationship and the customer table on the customerNumber column which is a many-to-one relationship.

5. customers table - this table contains customer data. This table has 13 columns. The customerNumber is the primary key and 
salesRepEmployeeNumber is the foreign key. This table has a relationship with the orders table on the customerNumber column which is a
one-to-many relationship, the payments table on the customerNumber column which is a one-to-one relationship and the employees table
on the employeeNumber column which is a many-to-one relationship.

6. payments table - this table contains payment data. This table has 4 columns. The customerNumber & checkNumber are both the 
composite key. This table has a relationship with the customers table on the customerNumber column which is a one-to-one relationship.

7. employees table - this table contains employee data. This table has 8 columns. The employeeNumber is the primary key and officeCode
is the foreign key. This table has a self-referencing relationship between the employeeNumber and reportsTo columns which is a
one-to-many relationship, a relationship with the customers table on the salesRepEmployeeNumber column which is a one-to- many relationship
and the offices table on teh officeCode column which is a many-to-one relationship.

8. offices table - this table contains office data. This table has 9 columns. The officeCode is the primary Key. This table has a 
relationship with the employees table on the officeCode table which is a one-to-many relationship.


-- SQL queries I will be executing to analyse the tables:

*/

SELECT "Customers" AS table_name,
	   13 AS number_of_attributes,
	   COUNT(*) AS number_of_rows
  FROM customers
  
 UNION 
  
SELECT "Products" AS table_name,
	   9 AS number_of_attributes,
	   COUNT(*) AS number_of_rows
  FROM products
  
 UNION
 
SELECT "ProductLines" AS table_name,
	   4 AS number_of_attributes,
	   COUNT(*) AS number_of_rows
  FROM productLines
  
 UNION
 
SELECT "Orders" AS table_name,
	    7 AS number_of_attributes,
		COUNT(*) AS number_of_rows
  FROM orders
  
 UNION

SELECT "OrderDetails" AS table_name,
       5 AS number_of_attributes,
	   COUNT(*) AS number_of_rows
  FROM orderdetails
  
 UNION
 
SELECT "Payments" AS table_name,
	   4 AS number_of_attributes,
	   COUNT(*) AS number_of_rows
  FROM payments
 
 UNION
 
SELECT "Employees" AS table_name,
	   8 AS number_of_attributes,
	   COUNT(*) AS number_of_rows
  FROM employees
  
 UNION
 
SELECT "Offices" AS table_name,
       9 AS number_of_attributes,
	   COUNT(*) AS number_of_rows
  FROM offices;


-- Write a query to compute the low stock for each product using a correlated subquery.

SELECT productcode, ROUND(SUM(quantityOrdered) * 1.0 / (SELECT quantityInStock
													      FROM products pr
													     WHERE od.productcode = pr.productCode), 2) AS low_stock
  FROM orderdetails od
 GROUP BY productCode
 ORDER BY low_Stock 
 LIMIT 10;

-- Write a query to compute the product performance for each product.

SELECT productCode, SUM(quantityOrdered * priceEach) AS product_performance
  FROM orderdetails
 GROUP BY productcode
 ORDER BY product_performance DESC
 LIMIT 10;
 
 