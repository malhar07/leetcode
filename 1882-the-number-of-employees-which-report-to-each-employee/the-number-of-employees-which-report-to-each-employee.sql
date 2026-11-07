/* Write your T-SQL query statement below */
select e2.employee_id, e2.name, count(e1.name) as reports_count,
ROUND(AVG(e1.age * 1.0),0) as average_age
FROM employees e1
LEFT JOIN employees e2
ON e1.reports_to = e2.employee_id
where e2.name is not NULL
Group by e2.name, e2.employee_id
having count(e1.name) >= 1
order by e2.employee_id;