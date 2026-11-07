/* Write your T-SQL query statement below */
select CONVERT(VARCHAR(7), trans_date, 120) AS month,
country,
count(id) AS trans_count,
SUM(case when state = 'approved' then 1 else 0 END) as approved_count,
SUM(amount) as Trans_total_amount,
SUM(case when state = 'approved' then amount else 0 END) as approved_total_amount
FROM Transactions
Group by
    CONVERT(VARCHAR(7), trans_date, 120),
    country;