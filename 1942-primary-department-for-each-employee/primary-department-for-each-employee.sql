/* Write your T-SQL query statement below */
WITH ranked_rows as (select employee_id,
department_id,
primary_flag,
ROW_NUMBER() OVER(Partition by employee_id order by primary_flag desc) as row_num
from employee)

select employee_id, department_id 
FROM ranked_rows
where row_num = 1;