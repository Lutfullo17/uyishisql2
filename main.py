#
# SELECT * FROM products
# WHERE category_id > 3
# SELECT * FROM customers
# WHERE country = 'Brazil' and country LIKE '__a%';
# SELECT * FROM customers
# WHERE country = 'UK' and company_name like '%a__'
# SELECT AVG(unit_price) FROM products
# SELECT * FROM orders
# WHERE shipped_date > required_date
# AND order_date BETWEEN '1997-07-01' AND '1997-07-31';
# SELECT MAX(category_id) FROM products
# WHERE category_id = 1
# SELECT * FROM products
# WHERE category_id = 3
# AND
# unit_price = (
#     SELECT MIN(unit_price)
# FROM products
# WHERE category_id = 3
# )
# SELECT * FROM ORDERS
# WHERE shipped_date > required_date
# AND order_date BETWEEN '1997-07-01' AND '1997-07-31';
# SELECT * FROM ORDERS
# WHERE shipped_date > require_date
# AND
# WHERE order_date BETWEEN '1997-02-01' AND '1197-02-27';
# INSERT INTO categories(category_id, category_name, description)
# VALUES
# ('9', 'test_category', 'cjnskjfnvnv')
# SELECT *
# FROM categories
# WHERE EXISTS (
#     SELECT *
#     FROM products
# WHERE products.category_id = categories.category_id
# );
#
# SELECT *
# FROM categories
#
# WHERE
# SELECT * FROM products
# products.product_name LIKE 'b%' AND category_id BETWEEN '2' AND '6'
# SELECT * FROM customers
# WHERE customers.country = 'USA'
# SELECT COUNT(*), to_char(order_date, 'YYYY-MM') FROM orders
# WHERE shipped_date > required_date AND to_char(order_date, 'YYYY' ) ='1997'
# GROUP BY to_char(order_date, 'YYYY-MM')
# SELECT COUNT(*), to_char(order_date, 'YYYY-MM-DD') FROM orders
# WHERE to_char(order_date, 'YYYY-MM') = '1997-03'
# GROUP BY to_char(order_date, 'YYYY-MM-DD')
# SELECT COUNT(*), to_char(order_date, 'YYYY-MM') FROM orders
# WHERE to_char(order_date, 'YYYY') = '1997' AND
# HAVING COUNT(*) > 10
# GROUP BY to_char(order_date, 'YYYY-MM')
# SELECT c.category_name
# FROM categories c
# WHERE EXISTS (
#     SELECT 1
# FROM products p
# WHERE p.category_id = c.category_id
# GROUP BY p.category_id
# HAVING COUNT(*) > 10
# );
# SELECT category_name, product_name FROM products p
# INNER JOIN categories c ON(p.category_id = c.category_id)
# SELECT order_date, order_id, company_name FROM orders o
# INNER JOIN customers c ON (o.customer_id = c.customer_id)
# WHERE to_char(order_date, 'YYYY-MM') = '1997-07'
# SELECT COUNT(product_id), category_name FROM products p
# INNER JOIN categories c ON(c.category_id = p.category_id)
# GROUP BY category_name
#
#
# SELECT product_name, category_id FROM products p
# INNER JOIN order_details od ON(p.product_id = od.product_id)
# INNER JOIN orders o ON(od.order_id = o.order_id)
# INNER JOIN customers c ON(o.customer_id = c.customer_id)
# WHERE category_id = 1 and to_char(order_date, 'YYYY-MM') = '1996-08'
#
#
# SELECT company_name  FROM customers c
# INNER JOIN orders o ON(c.customer_id = o.customer_id)
# INNER JOIN order_details od ON(o.order_id = od.order_id)
# INNER JOIN products p ON(od.product_id = p.product_id)
# WHERE
# c.country = 'USA' AND to_char(order_date, 'YYYY') = '1996'
#
# SELECT e.first_name, e.last_name, COUNT(order_id) FROM employees e
# INNER JOIN orders o ON(e.employee_id = o.employee_id)
# WHERE to_char(order_date, 'YYYY') = '1997'
# GROUP BY to_char(order_date, 'MM')
#
# SELECT o.order_id, SUM(od.unit_price * od.quantity * (1 - od.discount)) AS total_cost
# FROM orders o
# JOIN order_details od
# ON o.order_id = od.order_id
# WHERE EXTRACT(YEAR FROM o.order_date) = 1996
# GROUP BY o.order_id
# HAVING SUM(od.unit_price * od.quantity * (1 - od.discount)) > 10;
# SELECT MIN(product_name) FROM products p
# INNER JOIN suppliers s ON(p.supplier_id = s.supplier_id)
# WHERE category_id = 3
# GROUP BY s.company_name
#
#
# SELECT first_name FROM employees e
# INNER JOIN orders o ON(e.employee_id = o.employee_id)
# INNER JOIN customers c ON(o.customer_id = c.customer_id)
# WHERE TO_CHAR(o.order_date, 'YYYY-MM') = '1998-03'
# SELECT MAX(product_name) FROM products p
# INNER JOIN order_details od ON(p.product_id = od.product_id)
# INNER JOIN orders o ON(od.order_id = o.order_id)
# WHERE TO_CHAR(o.order_date, 'YYYY') = '1998'
# GROUP BY od.quantity
#
#
# SELECT s.company_name, s.contact_name FROM suppliers s
# INNER JOIN products p ON(s.supplier_id = p.supplier_id)
# INNER JOIN order_details od ON(p.product_id = od.product_id)
# INNER JOIN orders o ON(od.order_id = o.order_id)
# INNER JOIN customers c ON(o.customer_id = c.customer_id)
# WHERE TO_CHAR(o.order_date, 'YYYY') = '1997' AND s.country = 'USA' AND c.country = 'USA'
# GROUP BY s.supplier_id
#
#
# SELECT e.first_name FROM employees e
# INNER JOIN orders o ON(e.employee_id = o.employee_id)
# INNER JOIN order_details od ON(o.order_id = od.order_id)
# INNER JOIN products p ON(od.product_id = p.product_id)
# WHERE p.category_id = 5 AND TO_CHAR(o.order_date, 'YYYY') = '1997'
# SELECT COUNT(order_id), ship_city FROM orders o
# WHERE TO_CHAR(o.order_date, 'YYYY') = '1997' AND ship_country = 'USA'
# GROUP BY TO_CHAR(o.order_date, 'MM'), o.ship_city
#
#
#
