/* Write your T-SQL query statement below */
select teacher_id, count(distinct subject_id) as cnt
FROM Teacher
Group by teacher_id;