# Write your MySQL query statement below
-- select a.unique_id, b.name from EmployeeUNI a 
-- left join employees b on a.id = b.id 

-- union


-- select a.unique_id, b.name from EmployeeUNI a 
-- right join employees b on a.id = b.id;
-- SELECT a.unique_id, b.name
-- FROM EmployeeUNI a
-- RIGHT JOIN employees b ON a.id = b.id;

SELECT a.unique_id, b.name
FROM employees b
left JOIN EmployeeUNI a ON a.id = b.id;
