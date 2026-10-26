CREATE TABLE employees(
    employee_id INT PRIMARY KEY,
    employee_name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary NUMERIC(12,2) NOT NULL,
    hire_date DATE NOT NULL
);
CREATE TABLE customers(
    customer_id INT PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email TEXT,
    county TEXT,
    signup_date DATE NOT NULL
);

CREATE TABLE products(
product_id INT PRIMARY KEY,
product_name TEXT NOT NULL,
category TEXT NOT NULL,
unit_price NUMERIC(12,2) NOT NULL,
unit_cost NUMERIC (12,2) NOT NULL
);

CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL reference customers(customer_id),
    order_date DATE NOT NULL,
    status TEXT NOT NULL,
    amount NUMERIC (12,2) NOT NULL default 0
);

CREATE TABLE order_items(
    order_items_id  SERIAL PRIMARY KEY,
    order_id INT NOT NULL reference orders(order_id),
    product_id INT NOT NULL reference products(product_id),
    quantity INT NOT NULL,
    unit_price NUMERIC (12,2) NOT NULL

);

INSERT INTO employees
VALUES 
(1, 'Achieng Ouma', 'sales', 85000, '01-01-2002'),
(2, 'James Kimani', 'sales', 120000, '01-02-2002'),
(3,'Bony Face','sales', 35000, '02-02-2002'),
(4, 'Naomi Marry', 'it', 34557, '03-04-2002'),
(5, 'Nuunow Manny', 'it', 345678, '05-06-2002'),
(6,'Mansuur Abdi', 'sales', 345678, '05-05-2002');


INSERT INTO customers
VALUES
(4,'Maliyow', 'sdfghhj@gmail.com', 'Bondo','2004-09-14'),
(6,'Maliza', 'ertyu@gmail.com', 'kisumu','2004-09-07'),
(3, 'Yussuf', 'ukkllm@gmail.com', 'Mombasa','2004-09-05'),
(1, 'Akoo', 'ertyu@gmail.com', 'Nairobi','2004-09-04'),
(2, 'Lala', 'lalaa@gmail.com', 'Garissa','2004-09-03'),
(5, 'Mane', 'mane@gmail.com', 'Mandera','2004-10-02');


INSERT INTO products
VALUES
(1, 'Maize floor 2kg', 'cereals', 230, 190),
(2, 'Wheat floor 3kg', 'cereals', 290, 390),
(3, 'Rice ', 'cereals', 230, 230),
(4, 'cooking oil', 'groceries', 560, 90),
(5, 'Redmi','Electronics',4660,4569),
(6, 'sufuria', 'Household', 345,567);


INSERT into orders (
    order_id,customer_id,order_date,status,amount

);
SELECT i,
1+((i*7 + i/12) %13),
DATE '02-03-2009' + ((i * 37) % 280),
case when i % 10 = 0 'cancelled' when i % 10 = 1 then 'pending'
Else 'completed' END,
0
FROM generate series (1,120) AS i;

INSERT INTO order_items(
    order_id,product_id,quantity,unit_price
    SELECT o.order_id,
    p.product_id,
    1+(o.order_id + p.product_id)% 4, 
    p.unit_price
    FROM orders o 
    CROSS JOINS generate series(0, 2) AS K
    JOINS products P ON P.product_id = 1+((o.order_id + K * 3)%10)
    WHERE K < 1 + (orders.order_id % 3);
    UPDATE orders o 
    SET amount = s. total
    FROM (SELECT order_id,SUM (quantity * unit_price) AS total )
    FROM order_items
    GROUP BY order_id
     ) s
     WHERE s.order_id = o.order_id;

     SELECT (SELECT count( * ) FROM employees) AS employees,
     (SELECT count( * ) FROM customers) AS customers,
     (SELECT count( * ) FROM products) AS products,
     (SELECT count( * ) FROM orders) AS orders,
     (SELECT count( * ) FROM order_items) AS order_items,



CREATE TABLE employees(
    employee_id INT PRIMARY KEY NOT NULL,
    employee_name VARCHAR (100) NOT NULL,
    salary NUMERIC(12,2) NOT NULL,
    email TEXT NOT NULL,
    hire_date DATE NOT NULL

);

INSERT INTO employees
VALUES
(1, 'Khalf', 123456.45, 'khalifkdb@gmail.com', '06-01-2026'),
(2, 'Sdfghjk', 1234567.50, 'asrtyu@gmail.com', '2026-02-02'),
(1, 'Caamir', 123457.45, 'lalaakdb@gmail.com', '10-01-2026');













































































