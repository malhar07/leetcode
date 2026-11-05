/* Write your T-SQL query statement below */

SELECT machine_id, ROUND((Sum
(
    CASE
        when activity_type = 'end'
        then timestamp
        else 0
    END
)
- SUM
(
    CASE
        when activity_type = 'start'
        then timestamp
        else 0
    END
))
/ count(distinct process_id), 3) AS processing_time
FROM Activity
group by machine_id;