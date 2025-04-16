SELECT * FROM main_table; 

-- Create a new table named 'subscription' with customer_id as the primary key,
-- and columns for membership type and total spend
CREATE TABLE subscription (
	customer_id INT PRIMARY KEY,
	membership_type VARCHAR(10),
    total_spend DECIMAL(20,1)
);

-- Modify the total_spend column to allow two decimal places instead of one
ALTER TABLE subscription
MODIFY COLUMN total_spend DECIMAL(20, 2);


-- Insert data into the 'subscription' table by selecting relevant columns from 'main_table'
-- Mapping: 'Customer ID' → customer_id, 'Membership Type' → membership_type, 'Total Spend' → total_spend
INSERT INTO subscription (customer_id, membership_type, total_spend)
SELECT `Customer ID`, `Membership Type`, `Total Spend`
FROM main_table;






-- Create a new table named 'engagement' with three columns
CREATE TABLE engagement (
    customer_id INT PRIMARY KEY,            -- Unique customer identifier
    average_rating DECIMAL(2, 1),           -- Average rating with one decimal precision
    discount_applied BOOLEAN                -- Whether a discount was applied (TRUE/FALSE)
);

-- Check the structure of the 'engagement' table to confirm it was created correctly
DESCRIBE engagement;

-- Insert relevant data from the 'main_table' into the 'engagement' table
INSERT INTO engagement (customer_id, average_rating, discount_applied)
SELECT `Customer ID`, `Average Rating`, `Discount Applied`
FROM main_table;

SELECT * FROM engagement;



CREATE TABLE satisfaction (
	id INT PRIMARY KEY AUTO_INCREMENT,
    satisfaction_level VARCHAR(20)
);

DESCRIBE satisfaction;

SELECT * FROM satisfaction;

SELECT DISTINCT `satisfaction Level`
FROM main_table;

DELETE FROM satisfaction;

INSERT INTO satisfaction (satisfaction_level)
SELECT DISTINCT `Satisfaction Level`
FROM main_table;

SELECT *
FROM main_table
WHERE `Satisfaction Level` = '';

UPDATE satisfaction
SET `satisfaction_level` = NULL
WHERE `satisfaction_level` = '';

CREATE TABLE city (
	id INT PRIMARY KEY AUTO_INCREMENT,
	city VARCHAR(20)
);

DESCRIBE city;

INSERT INTO city(city)
SELECT DISTINCT City
FROM main_table;

SELECT * FROM engagement;

SELECT * FROM satisfaction;

SELECT * FROM subscription;

SELECT * FROM city;

-- Add a new column 'satisfaction_id' to store foreign key referencing the 'satisfaction' table
ALTER TABLE main_table
ADD COLUMN satisfaction_id INT;

-- Add a new column 'city_id' to store foreign key referencing the 'city' table
ALTER TABLE main_table
ADD COLUMN city_id INT;

-- Update 'satisfaction_id' in 'main_table' by matching the textual 'Satisfaction Level' with the 'satisfaction_level' in the 'satisfaction' table
UPDATE main_table AS main
JOIN satisfaction AS s
  ON main.`Satisfaction Level` = s.satisfaction_level
SET main.satisfaction_id = s.id;

-- Update 'city_id' in 'main_table' by matching the textual 'City' with the 'city' column in the 'city' table
UPDATE main_table AS main
JOIN city AS c
  ON main.City = c.city
SET main.city_id = c.id;


ALTER TABLE main_table
DROP COLUMN City;

ALTER TABLE main_table
DROP COLUMN `Membership Type`;

ALTER TABLE main_table
DROP COLUMN `Total Spend`;

ALTER TABLE main_table
DROP COLUMN `Average Rating`;

ALTER TABLE main_table
DROP COLUMN `Discount Applied`;

ALTER TABLE main_table
DROP COLUMN `Satisfaction Level`;


SELECT * FROM engagement;

SELECT * FROM satisfaction;

SELECT * FROM subscription;

SELECT * FROM city;


ALTER TABLE engagement
ADD FOREIGN KEY (customer_id)
REFERENCES main_table(`Customer ID`)
ON DELETE SET NULL;


-- Modify the column to allow NULLs
ALTER TABLE engagement
MODIFY COLUMN customer_id INT NULL;

-- Add a foreign key to link 'Customer ID' in main_table with 'customer_id' in the engagement table.
-- If a record in engagement is deleted, the corresponding 'Customer ID' in main_table will be set to NULL.
ALTER TABLE main_table
ADD FOREIGN KEY (`Customer ID`) REFERENCES engagement(customer_id) ON DELETE SET NULL;

-- Add a foreign key to link 'Customer ID' in main_table with 'customer_id' in the subscription table.
-- Ensures consistency between customer records in both tables. Deletes set the foreign key to NULL.
ALTER TABLE main_table
ADD FOREIGN KEY (`Customer ID`) REFERENCES subscription(customer_id) ON DELETE SET NULL;

-- Add a foreign key to connect satisfaction_id in main_table to the id in the satisfaction table.
-- If a satisfaction record is removed, main_table will reflect this with a NULL in satisfaction_id.
ALTER TABLE main_table
ADD FOREIGN KEY (satisfaction_id) REFERENCES satisfaction(id) ON DELETE SET NULL;

-- Add a foreign key linking city_id in main_table to the id in the city table.
-- Automatically sets city_id to NULL in main_table if the referenced city is deleted.
ALTER TABLE main_table
ADD FOREIGN KEY (city_id) REFERENCES city(id) ON DELETE SET NULL;




-- THEME:
	-- Unlocking Customer Value and Loyalty
    
-- Goal: Use customer behavior and satisfaction data to identify patterns in loyalty and spending habits, 
-- and uncover where the business can improve retention and revenue.


-- Identify the top 5 highest spending customers and their membership tier.
-- This helps highlight which membership types are bringing in big spenders.

SELECT s.customer_id, m.Gender, m.Age, s.membership_type, s.total_spend
FROM subscription AS s
JOIN main_table AS m
	ON s.customer_id = m.`Customer ID`
ORDER BY total_spend DESC
LIMIT 3;




-- Compare satisfaction levels across membership types.
-- This can reveal which tier is not just profitable, but also keeping customers happy.

SELECT s.membership_type, sat.satisfaction_level, COUNT(sat.satisfaction_level) AS satisfaction_count
FROM subscription AS s
JOIN main_table AS m
	ON s.customer_id = m.`Customer ID`
JOIN satisfaction AS sat
	ON m.satisfaction_id = sat.id
WHERE m.satisfaction_id = 8
GROUP BY s.membership_type;
    




-- Find the city with the most dissatisfaction to target service improvements.

SELECT c.city, sat.satisfaction_level, COUNT(sat.satisfaction_level) AS satisfaction_count
FROM main_table AS m
JOIN satisfaction AS sat
	ON m.satisfaction_id = sat.id
JOIN city AS c
	ON m.city_id = c.id
WHERE sat.id = 10
GROUP BY c.city;




-- Test if using discounts leads to more purchases.

SELECT SUM(m.`Items Purchased`) AS Total_Items_Purchased, e.discount_applied
FROM main_table AS m
JOIN engagement AS e
	ON m.`Customer ID` = e.customer_id
GROUP BY discount_applied;




-- Explore if unhappy customers take longer to return.

SELECT AVG(m.`Days Since Last Purchase`) AS Days_Since_Last_Purchased_AVG, sat.satisfaction_level
FROM main_table AS m
JOIN satisfaction AS sat
	ON m.satisfaction_id = sat.id
GROUP BY sat.satisfaction_level;



-- Build a profile of your dream customer: high spender + satisfied.
-- Helps marketing know who to attract more of.
SELECT m.`Customer ID`, m.Gender, m.Age, c.city, sub.membership_type, sub.total_spend
FROM main_table AS m
JOIN satisfaction AS s ON m.satisfaction_id = s.id
JOIN subscription AS sub ON m.`Customer ID` = sub.customer_id
JOIN city AS c ON m.city_id = c.id
WHERE s.satisfaction_level = 'Satisfied' AND sub.total_spend > 1000;