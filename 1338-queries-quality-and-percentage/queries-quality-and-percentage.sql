# Write your MySQL query statement below
select q1.query_name, Round(sum(q1.rating/q1.position)/count(q1.query_name),2) as quality, Round(((
    select count(*) from queries where query_name = q1.query_name and rating<3
)/count(q1.query_name)*100),2) as poor_query_percentage
from queries q1
group by query_name;