/* Write your T-SQL query statement below */
select s.user_id, 
COALESCE(ROUND(SUM(
    CASE 
        WHEN c.action = 'confirmed'
        THEN 1.0
        ELSE 0
    END
) / NULLIF( Count(c.user_id),0) , 2), 0) AS confirmation_rate
FROM signups s
left join confirmations c
on s.user_id = c.user_id
Group by s.user_id;