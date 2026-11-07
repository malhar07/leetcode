/* Write your T-SQL query statement below */
Select r.contest_id, Round(count( distinct r.user_id)*100.0 / (select count(*) FROM users), 2) AS percentage
FROM Register r
Group by r.contest_id
order by percentage desc, r.contest_id;