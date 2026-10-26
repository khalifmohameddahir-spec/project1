
"""
creation of database
CREATE DATABASE customers_db
creation of table
CREATE TABLE customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone_number VARCHAR(50)
)

ALTER TABLE customers,
ADD COLUMN address INT,

DELETE DATABASE customers_db

INSERT INTO customers_db
(customer_id, customer_name, email, phone_number)

VALUES
(1, OUMA, ouma254@email.com, 08678904567, 20),
(2, Isaac, brelsing@gmail.com, 0678903628, 10)

"""


CREATE DATABASE sales_db
creation of table 
CREATE TABLE customers(
    customer_name VARCHAR(13),
    city TEXT VARCHAR(23),
    ratio INT VARCHAR(23),
    phone_number INT VARCHAR(20)
);

ALTER TABLE customers,
ADD COLUMN profit INT

INSERT DATABASE sales_db
(customer_name, city, ratio, phone_number)

VALUES
(Akoo, Turkana, 17%, 3456789)





DROP customer_name



UPDATE TABLE customers,
SET city = "Bondo",
WHERE customer_name = "Akoo";



select * from customers

select customer_name, city
from customers,
SET ratio = 20%;
WHERE customer_id = 2;

































