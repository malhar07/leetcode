/* Write your T-SQL query statement below */
select activity_date as day, count(distinct user_id) as active_users
FROM Activity 
WHERE DATEDIFF(DAY, activity_date, '2019-07-27') >= 0
  AND DATEDIFF(DAY, activity_date, '2019-07-27') < 30
Group by activity_date;