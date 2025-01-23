-- Select all records from the Category table
SELECT * FROM Category;

-- Select specific columns from the Product table
SELECT ID, Name, Price FROM Product;

-- Select products with a price greater than 100
SELECT * FROM Product WHERE Price > 100;

-- Select all products sorted by price in descending order
SELECT * FROM Product ORDER BY Price DESC;

-- Count the number of products in each category
SELECT Category, COUNT(*) AS ProductCount FROM Product GROUP BY Category;

-- Join Product and Category tables to get product details along with category names
SELECT p.ID, p.Name, p.Price, c.CategoryName
FROM Product p
JOIN Category c ON p.CategoryID = c.ID;

-- Select products with a price higher than the average price
SELECT * FROM Product WHERE Price > (SELECT AVG(Price) FROM Product);

-- Use a CTE to find the top 5 most expensive products
WITH TopProducts AS (
    SELECT *, ROW_NUMBER() OVER (ORDER BY Price DESC) AS RowNum
    FROM Product
)
SELECT * FROM TopProducts WHERE RowNum <= 5;