# Write your MySQL query statement below
select name
from employee 
inner join 
(select e.managerId 
from employee e
group by e.managerId
having count(e.managerId)>=5) grouped
on employee.id = grouped.managerid;