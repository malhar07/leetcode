/* Write your T-SQL query statement below */
with login_nextday as (
    select player_id,
    event_date,
    LEAD(event_date) OVER(partition by player_id order by event_date) As next_day,
    RANK() OVER (partition by player_id order by event_date) AS Rank_
    FROM Activity
)
select Round(Sum(case when DAtediff(Day, event_date, next_day) = 1 then 1 else 0 end) * 1.00 /
       count(distinct player_id), 2) as fraction
       from login_nextday
       where Rank_ = 1;