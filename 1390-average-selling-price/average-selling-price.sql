/* Write your T-SQL query statement below */
SELECT p.product_id, ISNULL(ROUND(SUM(p.price*u.units)*1.0 / NULLIF(SUM(u.units), 0),2), 0) AS average_price
FROM prices p
left join unitssold u
ON p.product_id = u.product_id
AND u.purchase_date between p.start_date and p.end_date
Group by p.product_id;