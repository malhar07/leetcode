/* Write your T-SQL query statement below */
select class
FROM courses
Group by class
having count(distinct student) >= 5;