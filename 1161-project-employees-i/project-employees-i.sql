/* Write your T-SQL query statement below */
select p.project_id, Round(SUM(e.experience_years)*1.0/NULLIF(Count(e.employee_id), 0), 2) AS average_years
FROM project p
Left join employee e
ON p.employee_id = e.employee_id
Group by p.project_id;