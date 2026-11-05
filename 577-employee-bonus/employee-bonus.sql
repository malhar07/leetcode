/* Write your T-SQL query statement below */
SELECT e.name, b.bonus
FROM Employee e
LEft Join Bonus b
ON e.empId = b.empId
where bonus is NULL or bonus < 1000;