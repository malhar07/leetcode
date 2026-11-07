/* Write your T-SQL query statement below */
Select r.contest_id, Round(count( distinct u.user_id)*100.0 / (select count(*) FROM users), 2) AS percentage
FROM Register r
Left Join users u
On u.user_id = r.user_id
Group by r.contest_id
order by percentage desc, r.contest_id;
