/* Write your T-SQL query statement below */
With ranked_year_sales as (select product_id, year, quantity, price,
RANK() OVER(partition by product_id order by year) as rnk
FROM Sales)

select product_id, 
year as first_year,
quantity,
price
FROM ranked_year_sales
where rnk = 1;