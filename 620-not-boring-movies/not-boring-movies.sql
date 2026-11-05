/* Write your T-SQL query statement below */
Select * FROM Cinema
where id%2 = 1 
AND description not like 'boring'
order by rating desc;