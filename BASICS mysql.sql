#ORDER matters in mysql
SELECT
FROM
WHERE
ORDER BY
limit



"""
RETURN all the products
SELECT names, new price, unit_price * 1.1 AS new_price
FROM products table 
"""


#WHERE ,WHERE NOT
AND, OR, NOT



SELECT *
FROM order_items

WHERE order_items = 6 AND unit_price * quantity > 30


#IN, NOT IN 
WE use when comparing attribute with a list of values

eg
WHERE state IN ("va", "ka","ha")

instead of state = "va", OR state = "ka",OR state = "ha"


#THE BETWEEN operator
eg 
WHERE points >= 100 AND points <= 300

WHERE points BETWEEN 100 AND 300



#THE LIKE operator -is an older operator of mysql

eg 
WHERE last_name LIKE "%b" -ends with _b
WHERE last_name LIKE "%b%" - that contains _b anywhere
     
     or 
WHERE last_name LIKE "_b"

# % any number of character 
# _ single character




#THE REGEXP operator -MEANS Regular Expresion

same as LIKE operator but is like advance

eg
WHERE last_name REGEXP "b"

WHERE last_name REGEXP "b$" -ends with _b
WHERE last_name REGEXP "^b" - first_name must start with _b
''      '''      '''   "[fa]b" -
 |--vertical bar  -logical OR 
 [] - TO match any single character inside it
[a-h] -range



#THE is NULL operation


#The ORDER BY clause


#The limit clause

#INNER JOINS

# JOINING ACROSS DATABASES


#SELF JOINS 















