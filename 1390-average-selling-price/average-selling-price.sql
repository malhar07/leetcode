/* Write your T-SQL query statement below */
 With order_history AS (
    select u.product_id, u.units, p.price*u.units AS TotalPrice
    FROM unitsSold u
    JOIN Prices p
    ON u.product_id = p.product_id AND
    u.purchase_date between p.start_date and p.end_date
 )

 select p.product_id, ISNULL(ROUND(SUM(TotalPrice)*1.0/ NULLIF(SUM(units), 0), 2), 0) AS average_price
 FROM Prices p
 LEFT join Order_history o
 ON p.product_id = o.product_id
  Group by p.product_id;