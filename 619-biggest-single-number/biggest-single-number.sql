/* Write your T-SQL query statement below */
select MAX(num) as num 
FROM(
select num
FROM Mynumbers
group by num
having count(*) = 1) as single_numbers;



-- SELECT MAX(num) AS num
-- FROM (
--     SELECT num
--     FROM MyNumbers
--     GROUP BY num
--     HAVING COUNT(*) = 1
-- ) AS single_numbers;
